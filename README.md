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
1. Download `.uf2` files according to your boards.
   - Raspberry Pi Pico W from [here](https://github.com/wirebits/PicoWQuack/releases/download/v1.0/raspberry_pi_pico_w.uf2).
   - Raspberry Pi Pico 2 W from [here](https://github.com/wirebits/PicoWQuack/releases/download/v1.0/raspberry_pi_pico2_w.uf2).
2. Copy the `.uf2` file into the respective board.
   - `RPI-RP2` for `Raspberry Pi Pico W` and `RP2350` for `Raspberry Pi Pico 2 W`.
   - When it is copied, then it disconnects automatically and reconnect as `PICOWQUACK`.
   - Means CircuitPython is successfully flashed in the `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W` board.
7. Done! Now, `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W` Board is flashed with `.uf2` file.

# 🔧Setup Essential Files for PicoWQuack
1. Download or Clone the Repository.
2. Open the folder.
   - Make sure that your `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W` board is connected to your PC/Laptop.
3. Copy `code.py` in the `PICOWQUACK`.
   - It ask for replacement of `code.py` file, then replace it.
   - It will overwrite in the `code.py` file.
4. Copy `boot.py` in the `PICOWQUACK`.
5. Copy `index.html` in the `PICOWQUACK`.
   - It ask for replacement of `index.html` file, then replace it.
   - It will overwrite in the `index.html` file.
   - After 2-3 minutes, an access point is created named `PicoWQuack` whose password is `picowquack`.
6. Done! Now, `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W` board is ready to use as `PicoWQuack`.

# 🛠️ Tweeks in `network.conf` and `boot.py`files
## `network.conf`
- There are three values : `ssid`, `password` and `ip`.
- Put the values in double quotes.
- Change as per required.
- Default values :
  1. ssid : `PicoWQuack`
  2. password : `picowquack`
  3. ip : `192.168.4.1`
## `boot.py`
- `boot.py` helps to hide / unhide mass storage device to work in stealth.
- In `boot.py`, replace `X` with any pin number available on the board in `LOC 7`.
- By default, the mass storage is hidden when `boot.py` is in `PICOWQUACK`.
- To show mass storage, put jumper wire between that pin number mentioned in `boot.py` and `GND` and press and release the `RST` or `RESET` button.
- To hide mass storage, just remove jumper wire between them and press and release the `RST` or `RESET` button.

# 🏃🏻‍♂Run PicoWQuack
1. Connect to that access point.
2. When connected successfully, open your browser and type the following IP - `192.168.4.1`.
3. Hit enter.
   - A webpage open like this :
<img width="1913" height="883" alt="PicoWQuack Web Interface" src="https://github.com/user-attachments/assets/e63cb21f-3c4f-43fc-bea5-6d48f7759adc" />

4. Type your script and click on `Run` button.
   - The script executes!
5. By clicking `Upload` button, we can load `.txt` file and it show in text area and then we can run that script by clicking on `Run` button.
6. By clicking `Save` button, we can save mnemonics in text area on the system in `.txt` file.
7. By clicking `Clear` button, we can clear the text area.

> [!TIP]
> - Start your code with `WAIT` so that board get time to initiate.  
> - While using `LOOP` use only one command.  
> - If `LOOP` contain multiple commands, put `WAIT` between them so that it add a small delay between them.

# 🧹Clean `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W`
1. Connect `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W` with a USB cable.
2. Press and hold the `BOOTSEL` button and connect to the PC/Laptop.
   - When it connects, then `Raspberry Pi Pico W` or `Raspberry Pi Pico 2 W` show as a removable storage device named `RPI-RP2` or `RP2350` respectively.
   - When `RPI-RP2` or `RP2350` is showing, then release the `BOOTSEL` button.
3. Copy the `flash_nuke.uf2` file in the `RPI-RP2` or `RP2350`.
   - When it is copied, then it disconnects automatically and reconnect as `RPI-RP2` or `RP2350`.

# 🧩CIRCUITPY Directory Structure
- **CIRCUITPY/**
  - **lib/**
      - `adafruit_hid`
      - `adafruit_httpserver`
  - `code.py`
  - `index.html`

# 💡Mnemonic Table
| Mnemonics | Description | Example  |
|-----------|-------------|----------|
| WAIT      | It add time in the code.<br>Time is in milliseconds.<br>1000 ms = 1 second. | WAIT 1000 |
| TYPE      | It add text want to type in the code. | TYPE Hello World! |
| LOOP      | It runs commands for a certain number of times.<br> Synatx is `LOOP number-of-times commands` | LOOP 3<br>TYPE Hello World!<br>EXIT<br><br>LOOP 4<br>TAB<br>EXIT<br><br>LOOP 1<br>CTRL S<br>EXIT<br><br>LOOP 1<br>CTRL SHIFT N<br>EXIT<br> |
| INF       | It run commans infinitely.<br>Syntax is `INF commands` | INF<br>TYPE Hello World!<br>EXIT<br><br>INF<br>TAB<br>EXIT<br> |

# 📝Supported Mnemonics
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

# 📖Examples
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
