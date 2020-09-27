#!/usr/bin/env python3

import shutil, psutil, socket
import smtplib, os
from email.mime.text import MIMEText
from email.message import EmailMessage

def email(body):
  msg = EmailMessage()
  msg.set_content(body)
  msg['Subject'] = 'Upload Completed - Online Fruit Store'
  msg['From'] = 'automation@example.com'
  msg['To'] = 'student-00-9f38004092b9@example.com'
  text = msg.as_string()
  server = smtplib.SMTP('localhost')
  server.sendmail('automation@example.com', 'student-00-9f38004092b9@example.com', text)
  server.quit

# email when cpu is above 80%
if psutil.cpu_percent() > 0.8:
  email("Error - CPU usage is over 80%")

# email when disk space is less than 20%
free = shutil.disk_usage("/").free
total = shutil.disk_usage("/").total
if free < total//5:
  email("Error - Available disk space is less than 20%")

# email when memory is less than 500MB
avm = psutil.virtual_memory().available
if free < 500000000:
  email("Error - Available memory is less than 500MB")

# email when network is unreachable
if not socket.gethostbyname('localhost') == '127.0.0.1':
  email("Error - localhost cannot be resolved to 127.0.0.1")
