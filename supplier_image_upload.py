#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
images_path = "/home/student-00-9f38004092b9/supplier-data/images"

for i in os.listdir(images_path):
    if i.endswith("jpeg"):
        with open(images_path + "/" + i, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
