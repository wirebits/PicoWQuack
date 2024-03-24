# PicoWQuack
Setup for Raspberry Pi Pico W to make a Wifi Duck.

# This project is only working for Raspberry Pi Pico W!

# Credits
- The mnemoics used in this tool is heavily inspired by [Hak5](https://github.com/hak5) Ducky Script.
- The main inspiration of this project is from [Spacehuhn](https://github.com/SpacehuhnTech).
- The implementation of the wifi duck into Raspberry Pi Pico W inspired me by [dbisu](https://github.com/dbisu).

# Key Features
- Minimal Setup.
- Simple and clean webpage for type scripts.
- When code executed, then it show an text *Executed!*.

# OS Support
- Windows 10
- Android

# Installation and Setup of Circuit Python
1. Download Circuit Python `.uf2` file for Raspberry Pi Pico W from [here](https://downloads.circuitpython.org/bin/raspberry_pi_pico_w/en_US/adafruit-circuitpython-raspberry_pi_pico_w-en_US-8.2.10.uf2).
2. Connect Raspberry Pi Pico with a USB cable.
3. Press and hold the `BOOTSEL` button and connect to the PC/Laptop.
- When it connects, then Raspberry Pi Pico W show as a removable storage device named `RPI-RP2`.
- When `RPI-RP2` is showing, then release the `BOOTSEL` button.
4. Copy the `uf2` file in the `RPI-RP2`.
- When it is copied, then it disconnects automatically and reconnect as `CIRCUITPY`.
- Means circuit python is successfully flashed in the Raspberry Pi Pico W.
5. Open `CIRCUITPY`.
- There are two important things in it : `lib` folder and `code.py` file.
6. Download Adafruit CircuitPython Bundle from [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20240301/adafruit-circuitpython-bundle-8.x-mpy-20240301.zip).
7. Extarct the ZIP file.
8. Copy `adafruit_hid` and `adafruit_httpserver` folders in the `lib` folder of `CIRCUITPY`.
9. Done! Now, Raspberry Pi Pico W is ready to use as a Wifi Duck.

# Mnemonic Table
<table>
 <tr>
  <th>Mnemonics</th>
  <th>Description</th>
  <th>Example</th>
 </tr>
 <tr>
  <th>WAIT</th>
  <th>It add time in the code.<br>Time is in milliseconds.<br>1000 ms = 1 second.</th>
  <th>WAIT 1000</th>
 </tr>
 <tr>
  <th>TYPE</th>
  <th>It add text want to type in the code.</th>
  <th>TYPE Hello World!</th>
 </tr>
</table>

# Install and Run
1. Download or Clone the Repository.
2. Open the folder.
3. There are two files in it : `code.py` and `index.html`.
- Make sure that your Raspberry Pi Pico W is connected to your PC/Laptop.
4. Copy both files in the `CIRCUITPY`.
- It ask for replacement of `code.py` file, then replace it.
- It will overwrite in the `code.py` file.
- After 2-3 minutes, an Access Point is created named `PicoWQuack` whose password is `picowquack`.
6. Connect to that access point.
7. When connected successfully, open your browser and type the following IP - `192.168.4.1`.
8. Hit enter.
- A webpage open like this :

![PicoWQuack Web Page](https://github.com/wirebits/PicoWQuack/assets/159493381/5748b157-58ed-4ecf-af2a-4d60cd53bbde)

9. Type your script and click on Run button.
- The script executes!

# Note
Add a space by press `SPACE` key at the end of the script.

# Before Coding...
Start your code with `WAIT` so that board get time to initiate.

# Examples
## Open notepad and type Hello World!

```
WAIT 1000
GUI R
WAIT 1000
TYPE notepad
WAIT 1000
ENTER
WAIT 1000
TYPE Hello World! 
```
## Open CMD as Administrator Mode

```
WAIT 1000
GUI R
WAIT 1000
TYPE cmd
WAIT 1000
CTRL SHIFT ENTER
WAIT 1300
ALT Y 
```
