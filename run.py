#!/usr/bin/env python3

import os
import requests
import json

images_path = "/home/student-00-9f38004092b9/supplier-data/images"
json_path = "/home/student-00-9f38004092b9/supplier-data/descriptions"
url = "http://35.225.56.116/fruits/?format=api"
headers = {'Content-type': 'application/json'}

for i in os.listdir(images_path):
  if i.endswith("jpeg"):
    with open(json_path + "/" + i[:3] + ".txt", 'r') as f:
      ln = f.readlines()
      data = json.dumps({"name": ln[0].strip(), "weight": int(ln[1].strip()[:3]), "description": ln[2].strip(), "image_name": i})
      print(requests.post(url, data=data, headers=headers))
