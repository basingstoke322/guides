import socket
import time
from cairosvg import svg2png
import cv2
from pyzbar import pyzbar
from PIL import Image
from io import BytesIO
import hashlib
import base64

timeout = 0.3

sock = socket.socket()
sock.connect(("localhost", 10014))
while True:
    time.sleep(timeout)
    res = sock.recv(40960).decode()
    try:
        png = base64.b64decode(max(res.split('\n'), key=len).strip())
        with open("res.png", 'wb') as f:
            f.write(png)
        img = cv2.imread('res.png')
        data = pyzbar.decode(img)[0][0]
        print(data)
        sock.send(data)
    except Exception:
        print(res)
        break
