# PicoWQuack
# Setup for Raspberry Pi Pico W to make a Wifi Duck.
# Author - WireBits

import wifi
import time
import usb_hid
import socketpool
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_httpserver import Server, Request, JSONResponse, POST, Response

ssid = "PicoWQuack"
password = "picowquack"

wifi.radio.stop_station()
wifi.radio.start_ap(ssid, password)

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/", debug=True)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

hidKeys = {
    'A': Keycode.A, 'B': Keycode.B, 'C': Keycode.C, 'D': Keycode.D, 'E': Keycode.E,
    'F': Keycode.F, 'G': Keycode.G, 'H': Keycode.H, 'I': Keycode.I, 'J': Keycode.J,
    'K': Keycode.K, 'L': Keycode.L, 'M': Keycode.M, 'N': Keycode.N, 'O': Keycode.O,
    'P': Keycode.P, 'Q': Keycode.Q, 'R': Keycode.R, 'S': Keycode.S, 'T': Keycode.T,
    'U': Keycode.U, 'V': Keycode.V, 'W': Keycode.W, 'X': Keycode.X, 'Y': Keycode.Y,
    'Z': Keycode.Z, 'F1': Keycode.F1, 'F2': Keycode.F2, 'F3': Keycode.F3, 'F4': Keycode.F4,
    'F5': Keycode.F5, 'F6': Keycode.F6, 'F7': Keycode.F7, 'F8': Keycode.F8, 'F9': Keycode.F9,
    'F10': Keycode.F10, 'F11': Keycode.F11, 'F12': Keycode.F12, 'LEFT': Keycode.LEFT_ARROW,
    'UP': Keycode.UP_ARROW, 'RIGHT': Keycode.RIGHT_ARROW, 'DOWN': Keycode.DOWN_ARROW,
    'TAB': Keycode.TAB, 'HOME': Keycode.HOME, 'END': Keycode.END, 'PGUP': Keycode.PAGE_UP,
    'PGDN': Keycode.PAGE_DOWN, 'CAPS': Keycode.CAPS_LOCK, 'NUM': Keycode.KEYPAD_NUMLOCK,
    'SCROLL': Keycode.SCROLL_LOCK, 'CTRL': Keycode.CONTROL, 'SHIFT': Keycode.SHIFT, 'ALT': Keycode.ALT,
    'GUI': Keycode.GUI, 'ESC': Keycode.ESCAPE, 'PRTSCR': Keycode.PRINT_SCREEN, 'PAUSE': Keycode.PAUSE,
    'SPACE': Keycode.SPACE, 'DEL': Keycode.DELETE, 'INSERT': Keycode.INSERT, 'BKSP': Keycode.BACKSPACE,
    'ENTER': Keycode.ENTER, 'APP': Keycode.APPLICATION
}

def convertHID(hidLine):
    newline = []
    for key in filter(None, hidLine.split(" ")):
        key = key.upper()
        command_keycode = hidKeys.get(key, None)
        if command_keycode is not None:
            newline.append(command_keycode)
        elif hasattr(Keycode, key):
            newline.append(getattr(Keycode, key))
        else:
            print("Unknown key! Try another key!")
    return newline

def keyTrigger(hidLine):
    for kd in hidLine:
        kbd.press(kd)
    kbd.release_all()

def typeText(hidLine):
    layout.write(hidLine)

def generateHID(hidLine):
    if hidLine.startswith("WAIT"):
        time.sleep(float(hidLine.split(" ")[1]) / 1000)
    elif hidLine.startswith("TYPE"):
        typeText(hidLine.split(" ", 1)[1])
    elif hidLine.startswith("LOOP"):
        parts = hidLine.split(" ", 2)
        loop_count = int(parts[1])
        command = parts[2]
        for _ in range(loop_count):
            if command.startswith("TYPE"):
                generateHID(command + "\n")
            else:
                generateHID(command)
    elif hidLine.startswith("INF"):
        parts = hidLine.split(" ", 1)
        command = parts[1]
        while True:
            if command.startswith("TYPE"):
                generateHID(command + "\n")
            else:
                generateHID(command)
    else:
        newScriptLine = convertHID(hidLine)
        keyTrigger(newScriptLine)

progStatus = False
defaultDelay = 0

def hid_execute(hidScript):
    global progStatus
    if not progStatus:
        for hidLine in hidScript:
            hidLine = hidLine.rstrip()
            generateHID(hidLine)
            time.sleep(float(defaultDelay) / 1000)
        print("Done")
    else:
        print("Update your payload and start again!")

def handle_index_html(request):
    with open("index.html", "r") as file:
        index_html_content = file.read()
    return Response(request, body=index_html_content, headers={"Content-Type": "text/html"})

@server.route("/")
def base(request: Request):
    return handle_index_html(request)

@server.route("/execute", POST, append_slash=True)
def execute(request: Request):
    if request.method == POST:
        try:
            payload = request.json()["content"]
            if isinstance(payload, str):
                payload = payload.splitlines()
                hid_execute(payload)
                return JSONResponse(request, {"message": "Done"})
            else:
                return JSONResponse(request, {"message": "Invalid payload format"}, status_code=400)
        except Exception as e:
            print(f"Error handling request: {e}")
            return JSONResponse(request, {"message": "Error handling request"}, status_code=500)

try:
    server.serve_forever('192.168.4.1', 80)
except KeyboardInterrupt:
    print("Server stopped by user.")
