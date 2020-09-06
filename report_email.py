#!/usr/bin/env python3

import datetime, os

json_path = "/home/student-00-9f38004092b9/supplier-data/descriptions"
bbb = "Processed Update on " + str(datetime.datetime.now())
for i in os.listdir(json_path):
  if i.endswith("txt"):
    with open(json_path + "/" + i, 'r') as f:
      ln = f.readlines()
      bbb += "\n \n name: " +  ln[0].strip() + "\n weight: " + ln[1].strip()
      
emails.generate_email(bbb)
