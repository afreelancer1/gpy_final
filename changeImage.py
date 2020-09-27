#!/usr/bin/env python3

from PIL import Image
import os

images_path = "/home/student-00-9f38004092b9/supplier-data/images"
size = (600,400)

for i in os.listdir(images_path):
  if i.endswith("tiff"): #filtering out the image files
    im = Image.open(images_path + "/" + i)
    im = im.resize(size)
    im = im.convert("RGB")
    im.save(images_path + "/" + i[:3] + ".jpeg")
