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
server = Server(pool, "/static", debug=True)

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
    else:
        newScriptLine = convertHID(hidLine)
        keyTrigger(newScriptLine)

time.sleep(0.5)

progStatus = False
defaultDelay = 0

def hid_execute(hidScript):
    if not progStatus:
        duckyScript = hidScript
        for hidLine in duckyScript:
            hidLine = hidLine.rstrip()
            generateHID(hidLine)
            time.sleep(float(defaultDelay) / 1000)
        print("Done")
    else:
        print("Update your payload and start again!")

with open("index.html", "r") as file:
    index_html_content = file.read()

@server.route("/")
def base(request: Request):
    headers = {"Content-Type": "text/html"}
    return Response(request, body=index_html_content, headers=headers)

@server.route("/execute", POST, append_slash=True)
def execute(request: Request):
    if request.method == POST:
        req = request.json()
        payload = req["content"]
        payload = payload.splitlines()
        hid_execute(payload)
        return JSONResponse(request, {"message": "Done"})

server.serve_forever('192.168.4.1', 80)