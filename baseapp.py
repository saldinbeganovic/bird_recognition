import base64
import cv2
import glob
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import requests
import json
import os

Tk().withdraw()
load_image = askopenfilename()
api="http://127.0.0.1:5000/test"

with open(load_image, "rb") as f:
    im_bytes = f.read()
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

payload = json.dumps({"image": im_b64})
response = requests.post(api, data=payload, headers=headers)
try:
    data = response.text
    print(data)
except requests.exceptions.RequestException:
    print(response.text)