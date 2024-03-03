# PicoWQuack
# Setup for Raspberry Pi Pico W to make a Wifi Duck.
# Author - WireBits

import wifi
import socketpool
from hid import hid_execute, req_decode
from adafruit_httpserver import Server, Request, Response

ssid = "PicoWQuack"
password = "picowquack"

wifi.radio.start_ap(ssid, password)

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

with open("index.html", "r") as file:
    index_html_content = file.read()

@server.route("/")
def base(request: Request):
    headers = {"Content-Type": "text/html"}
    return Response(request, index_html_content, headers=headers)

@server.route("/decode", methods=["POST"])
def decode(request: Request):
    content_start = request.body.find(b"content=") + len("content=")
    content_end = request.body.find(b"&", content_start)
    file_content = request.body[content_start:content_end].decode()
    decoded_string = req_decode(file_content).replace("+", " ")
    final_script = decoded_string.splitlines()
    hid_execute(final_script)
    return Response(request, "Executed!")

server.serve_forever('192.168.4.1', 80)