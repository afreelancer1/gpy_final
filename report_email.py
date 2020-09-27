#!/usr/bin/env python3

import datetime, os

json_path = "/home/student-00-9f38004092b9/supplier-data/descriptions"
body = "Processed Update on " + str(datetime.datetime.now()) #adding current time to the string

for i in os.listdir(json_path):
  if i.endswith("txt"): #filtering out the txt files
    with open(json_path + "/" + i, 'r') as f:
      ln = f.readlines()
      body += "\n \n name: " +  ln[0].strip() + "\n weight: " + ln[1].strip() #parsing the txt file
      
emails.generate_email(body)
