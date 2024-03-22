# PicoWQuack
Setup for Raspberry Pi Pico W to make a Wifi Duck.

# This project is only working for Raspberry Pi Pico W!

# Credits
The mnemoics used in this tool is heavily inspired by <a href="https://github.com/hak5">Hak5</a> Ducky Script.<br>
The main inspiration of this project is from <a href="https://github.com/SpacehuhnTech">Spacehuhn</a>.<br>
The implementation of the wifi duck into Raspberry Pi Pico W inspired me by <a href="https://github.com/dbisu">dbisu</a>.

# Setup and Installation of Circuit Python
1. Download Circuit Python ```.uf2``` file for Raspberry Pi Pico W from <a href="https://downloads.circuitpython.org/bin/raspberry_pi_pico_w/en_US/adafruit-circuitpython-raspberry_pi_pico_w-en_US-8.2.10.uf2">here</a>.<br>
2. Connect Raspberry Pi Pico with a USB cable.<br>
3. Press and hold the bootsel button and connect to the PC/Laptop.<br>
-When it connects, then Raspberry Pi Pico W show as a removable storage device named ```RPI-RP2```.<br>
-When ```RPI-RP2``` is showing, then release the bootsel button.<br>
4. Copy the ```uf2``` file in the ```RPI-RP2```.<br>
-When it is copied, then it disconnects automatically and reconnect as ```CIRCUITPY```.<br>
Means circuit python is successfully flashed in the Raspberry Pi Pico W.
5. Open ```CIRCUITPY```.<br>
-There are two important things in it : ```lib``` folder and ```code.py``` file<br>
6. Download Adafruit CircuitPython Bundle from <a href="https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20240301/adafruit-circuitpython-bundle-8.x-mpy-20240301.zip">here</a>.<br>
7. Extarct the ZIP file.<br>
8. Copy ```adafruit_hid``` and ```adafruit_httpserver``` folders in the ```lib``` folder of ```CIRCUITPY```.<br>
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

# Tested Systems
The tool is currently tested on : <br>
1. Windows (10)<br>
The testing is going on different systems.

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder.<br>
3. There are two files in it : ```code.py``` and ```index.html```.<br>
-Make sure that your Raspberry Pi Pico W is connected to your PC/Laptop.<br>
4. Copy both files in the ```CIRCUITPY```.<br>
-It ask for replacement of ```code.py``` file, then replace it. It will overwrite in the ```code.py``` file.<br>
-After 2-3 minutes, an access point is created named ```PicoWQuack``` whose password is ```picowquack```.<br>
6. Connect to that access point.<br>
7. When connected successfully, open your browser and type the following IP - ```192.168.4.1```.<br>
8. Hit enter.<br>
-A webpage open like this : <br>

![photo_2024-03-04_02-46-57](https://github.com/wirebits/PicoWQuack/assets/159493381/5748b157-58ed-4ecf-af2a-4d60cd53bbde)

9. Type your script and click on Run button.<br>
-The script executes!<br>
-To code Raspberry Pi Pico W, use Thonny IDE.<br>

<h1>Key Features</h1>
<b>1. Simple and clean webpage for type scripts.</b><br>
<b>2. When code executed, then it show an text <i>Executed!</i>.<br>
