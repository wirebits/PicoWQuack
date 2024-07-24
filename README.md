# PicoWQuack
Setup for Raspberry Pi Pico W to make a Wifi Duck.

# This project is only working for Raspberry Pi Pico W!

# Working of PicoWQuack
![PicoWQuack Working](https://github.com/user-attachments/assets/eb3bbf7c-a71a-456f-b1df-3d3926cacfe6)

# What is Wifi Duck?
It is a USB Rubber Ducky with wifi capabilities and it was termed by [Spacehuhn](https://github.com/SpacehuhnTech).

# Credits
- The mnemoics used in this tool is heavily inspired by [Hak5](https://github.com/hak5) Ducky Script.
- The main inspiration of this project is from [Spacehuhn](https://github.com/SpacehuhnTech).
- The implementation of the wifi duck into Raspberry Pi Pico W inspired me by [dbisu](https://github.com/dbisu).

# Key Features
- Minimal Setup.
- Simple and clean webpage for type mnemonics.
- Run Button - Run typed mnemonics.
- Upload Button - Upload .txt files which contain mnemonics to run.
- Save Button - Save typed mnemonics on the system.

# OS Support
- Windows 10
- Android

# Installation and Setup of Circuit Python
1. Download Latest Circuit Python `.uf2` file for Raspberry P i Pico W - [here](https://circuitpython.org/board/raspberry_pi_pico_w/)
   - Latest version is **9.1.0**.
2. Connect Raspberry Pi Pico W with a USB cable.
3. Press and hold the `BOOTSEL` button and connect to the PC/Laptop.
   - When it connects, then Raspberry Pi Pico W show as a removable storage device named `RPI-RP2`.
   - When `RPI-RP2` is showing, then release the `BOOTSEL` button.
4. Copy the `.uf2` file in the `RPI-RP2`.
   - When it is copied, then it disconnects automatically and reconnect as `CIRCUITPY`.
   - Means circuit python is successfully flashed in the Raspberry Pi Pico W.
5. Open `CIRCUITPY`.
   - There are two important things in it : `lib` folder and `code.py` file.
6. Download Adafruit CircuitPython Bundle from [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)
   - Latest is `adafruit-circuitpython-bundle-9.x-mpy-20240709.zip`.
7. Extarct the ZIP file.
8. Go to the `lib` folder in the extracted ZIP file.
9. Copy `adafruit_hid` and `adafruit_httpserver` folders in the `lib` folder of `CIRCUITPY`.
10. Done! Now, Raspberry Pi Pico W is ready to use as a Wifi Duck.

# Mnemonic Table
| Mnemonics | Description | Example  |
|-----------|-------------|----------|
| WAIT      | It add time in the code.<br>Time is in milliseconds.<br>1000 ms = 1 second. | WAIT 1000 |
| TYPE      | It add text want to type in the code. | TYPE Hello World! |
| LOOP      | It runs commands for a certain number of times.<br> Synatx is `LOOP number-of-times commands` | LOOP 3 TYPE Hello World!<br>LOOP 4 TAB<br>LOOP 1 CTRL S<br>LOOP 1 CTRL SHIFT ENTER |
| INF       | It run commans infinitely.<br>Syntax is `INF commands` | INF TYPE Hello World!<br>INF TAB |

# Supported Mnemonics
## Alphabet Keys
`A` `B` `C` `D` `E` `F` `G` `H` `I` `J` `K` `L` `M` `N` `O`
`P` `Q` `R` `S` `T` `U` `V` `W` `X` `Y` `Z`
## Function Keys
`F1` `F2` `F3` `F4` `F5` `F6` `F7` `F8` `F9` `F10` `F11` `F12`
## Navigation Keys
`LEFT` `UP` `RIGHT` `DOWN` `TAB` `HOME` `END` `PGUP` `PGDN`
## Lock Keys
`CAPS` `NUM` `SCROLL`
## System and GUI Keys
`GUI` `ESC` `PRTSCR` `PAUSE`
## Editing Keys
`INSERT` `DEL` `BKSP` `ENTER`
## Modifier Keys
`CTRL` `SHIFT` `ALT`
## ASCII Characters
`` ` `` `!` `@` `#` `$` `%` `^` `&` `*` `(` `)` `-` `=` `[` `]` `\` `;` 
`'` `,` `.` `/` `SPACE` `~` `_` `+` `{` `}` `|` `:` `"` `<` `>` `?` `0`
`1` `2` `3` `4` `5` `6` `7` `8` `9`

# Install and Run
1. Download or Clone the Repository.
2. Open the folder.
3. There are two files in it : `code.py` and `index.html`.
   - Make sure that your Raspberry Pi Pico W is connected to your PC/Laptop.
5. Copy both files in the `CIRCUITPY`.
   - It ask for replacement of `code.py` file, then replace it.
   - It will overwrite in the `code.py` file.
   - After 2-3 minutes, an Access Point is created named `PicoWQuack` whose password is `picowquack`.
6. Connect to that access point.
7. When connected successfully, open your browser and type the following IP - `192.168.4.1`.
8. Hit enter.
   - A webpage open like this :

![PicoWQuack Web Page](https://github.com/user-attachments/assets/491b82fc-24ab-4e5d-a453-4edb04d30d23)

9. Type your script and click on `Run` button.
    - The script executes!
10. By clicking `Upload` button, we can load `.txt` file and it show in text area and then we can run that script by clicking on `Run` button.
11. By clicking `Save` button, we can save mnemonics in text area on the system in `.txt` file.

# Before Coding...
1. Start your code with `WAIT` so that board get time to initiate.
2. While using `LOOP` use only one command.

# Clean Raspberry Pi Pico W
1. Connect Raspberry Pi Pico W with a USB cable.
2. Press and hold the `BOOTSEL` button and connect to the PC/Laptop.
   - When it connects, then Raspberry Pi Pico W show as a removable storage device named `RPI-RP2`.
   - When `RPI-RP2` is showing, then release the `BOOTSEL` button.
3. Copy the `flash_nuke.uf2` file in the `RPI-RP2`.
   - When it is copied, then it disconnects automatically and reconnect as `RPI-RP2`.

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
## Create A New Folder
```
WAIT 1000
CTRL SHIFT N
WAIT 1200
TYPE hello
WAIT 1100
ENTER
```
