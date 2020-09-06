#!/usr/bin/env python3

import smtplib, os
from email.mime.text import MIMEText
from email.message import EmailMessage

def generate_email(bbb):
  msg = EmailMessage()
  body = bbb
  msg.set_content(body)
  msg['Subject'] = 'Upload Completed - Online Fruit Store'
  msg['From'] = 'automation@example.com'
  msg['To'] = 'student-00-9f38004092b9@example.com'
  filename = '/tmp/processed.pdf'
  with open(filename, 'rb') as content_file:
      content = content_file.read()
      msg.add_attachment(content, maintype='application/pdf', subtype='pdf', filename='processed.pdf')

  text = msg.as_string()
  server = smtplib.SMTP('localhost')
  server.sendmail('automation@example.com', 'student-00-9f38004092b9@example.com', text)
  server.quit

if __name__ == "__main__":
  generate_email()
