# PicoWQuack
# Setup for Raspberry Pi Pico W to make a Wifi Duck.
# Author - WireBits

import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def hid_execute(hidScript):
    hidKeys = {
    'A':Keycode.A,'B':Keycode.B,'C':Keycode.C,'D':Keycode.D,'E':Keycode.E,
    'F':Keycode.F,'G':Keycode.G,'H':Keycode.H,'I':Keycode.I,'J':Keycode.J,
    'K':Keycode.K,'L':Keycode.L,'M':Keycode.M,'N':Keycode.N,'O':Keycode.O,
    'P':Keycode.P,'Q':Keycode.Q,'R':Keycode.R,'S':Keycode.S,'T':Keycode.T,
    'U':Keycode.U,'V':Keycode.V,'W':Keycode.W,'X':Keycode.X,'Y':Keycode.Y,
    'Z':Keycode.Z,'F1':Keycode.F1,'F2':Keycode.F2,'F3':Keycode.F3,'F4':Keycode.F4,
    'F5':Keycode.F5,'F6':Keycode.F6,'F7':Keycode.F7,'F8':Keycode.F8,'F9':Keycode.F9,
    'F10':Keycode.F10,'F11':Keycode.F11,'F12':Keycode.F12,'LEFT':Keycode.LEFT_ARROW,
    'UP':Keycode.UP_ARROW,'RIGHT':Keycode.RIGHT_ARROW,'DOWN':Keycode.DOWN_ARROW,
    'TAB':Keycode.TAB,'HOME':Keycode.HOME,'END':Keycode.END,'PGUP':Keycode.PAGE_UP,
    'PGDN':Keycode.PAGE_DOWN,'CAPS':Keycode.CAPS_LOCK,'NUM':Keycode.KEYPAD_NUMLOCK,
    'SCROLL':Keycode.SCROLL_LOCK,'CTRL':Keycode.CONTROL,'SHIFT':Keycode.SHIFT,'ALT':Keycode.ALT,
    'GUI':Keycode.GUI,'ESC':Keycode.ESCAPE,'PRTSCR':Keycode.PRINT_SCREEN,'PAUSE':Keycode.PAUSE,
    'SPACE':Keycode.SPACE,'DEL':Keycode.DELETE,'INSERT':Keycode.INSERT,'BKSP':Keycode.BACKSPACE,
    'ENTER':Keycode.ENTER,'APP':Keycode.APPLICATION
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
        if(hidLine[0:3] == "REM"):
            pass
        elif(hidLine[0:5] == "INTVL"):
            time.sleep(float(hidLine[6:])/1000)
        elif(hidLine[0:5] == "WRITE"):
            typeText(hidLine[6:])
        else:
            newScriptLine = convertHID(hidLine)
            keyTrigger(newScriptLine)

    time.sleep(.5)

    progStatus = False
    defaultDelay = 0
    if(progStatus == False):
        previousLine = ""
        duckyScript = hidScript
        for hidLine in duckyScript:
            hidLine = hidLine.rstrip()
            if(hidLine[0:6] == "REPEAT"):
                for i in range(int(hidLine[7:])):
                    generateHID(previousLine)
                    time.sleep(float(defaultDelay)/1000)
            else:
                generateHID(hidLine)
                previousLine = hidLine
            time.sleep(float(defaultDelay)/1000)

        print("Done")
    else:
        print("Update your payload and start again!")

def req_decode(enc_string):
    dec_string = ""
    i = 0
    while i < len(enc_string):
        if enc_string[i] == '%':
            dec_char = chr(int(enc_string[i + 1:i + 3], 16))
            dec_string += dec_char
            i += 3
        else:
            dec_string += enc_string[i]
            i += 1
    return dec_string
