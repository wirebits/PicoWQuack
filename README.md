# 🦆PicoWQuack
A wifi-controlled USB Rubber Ducky clone built with Raspberry Pi Pico W Series boards.

# ✨Features
- Minimal Setup.
- Simple and clean webpage for type mnemonics.
- Run Button - Run typed mnemonics.
- Upload Button - Upload .txt files which contain mnemonics to run.
- Save Button - Save typed mnemonics on the system.
- Clear Button - Clears the text area.

# ✅Supported Boards
- Raspberry Pi Pico W
- Raspberry Pi Pico 2 W

# 📦Requirements
- `1` Raspberry Pi Pico W or Raspberry Pi Pico 2 W Board
- `1` Micro-B USB Cable with data transfer support

# ⚙️Setup CircuitPython
1. Open Official CircuitPython download link from [here](https://circuitpython.org/downloads).
2. Search `Pico W` or `Pico 2 W` according to the board you have.
3. Select your board and click on it.
4. Download latest stable release CircuitPython `.uf2` file and noted its version.
   - It is like X.Y.Z.
   - Latest stable release is `9.2.8` but it can be changed in future so keep eye on it.
5. Copy the `.uf2` file into the respective board.
   - When it is copied, then it disconnects automatically and reconnect as `CIRCUITPY`.
   - Means CircuitPython is successfully flashed in the `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W` board.
6. Done! Now, `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W` Board is flashed with CircuitPython `.uf2` file.

# ⚙️Setup Essential Files for PicoWQuack

# CIRCUITPY Directory Structure
- **CIRCUITPY/**
  - **lib/**
      - `adafruit_hid`
      - `adafruit_httpserver`
  - `code.py`
  - `index.html`

# Mnemonic Table
| Mnemonics | Description | Example  |
|-----------|-------------|----------|
| WAIT      | It add time in the code.<br>Time is in milliseconds.<br>1000 ms = 1 second. | WAIT 1000 |
| TYPE      | It add text want to type in the code. | TYPE Hello World! |
| LOOP      | It runs commands for a certain number of times.<br> Synatx is `LOOP number-of-times commands` | LOOP 3<br>TYPE Hello World!<br>EXIT<br><br>LOOP 4<br>TAB<br>EXIT<br><br>LOOP 1<br>CTRL S<br>EXIT<br><br>LOOP 1<br>CTRL SHIFT N<br>EXIT<br> |
| INF       | It run commans infinitely.<br>Syntax is `INF commands` | INF<br>TYPE Hello World!<br>EXIT<br><br>INF<br>TAB<br>EXIT<br> |

# Special Symbols
1. `-`
- It is used to put the cursor in the next line.
- It is only used with TYPE.
- Example : `TYPE Hello World!-`
- If TYPE contain any command and then `-` then it run automatically without `ENTER` key.

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

![PicoWQuack Web Page](https://github.com/user-attachments/assets/f4d342f4-74f8-426c-8b8c-693419043992)

9. Type your script and click on `Run` button.
    - The script executes!
10. By clicking `Upload` button, we can load `.txt` file and it show in text area and then we can run that script by clicking on `Run` button.
11. By clicking `Save` button, we can save mnemonics in text area on the system in `.txt` file.

> [!TIP]
>  Start your code with `WAIT` so that board get time to initiate.<br>
>  While using `LOOP` use only one command.

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
## Open notepad and type Hello World! 6 times in different lines
```
WAIT 1000
GUI R
WAIT 1000
TYPE notepad
WAIT 1000
ENTER
WAIT 1000
LOOP 6
TYPE Hello World!-
EXIT
```
