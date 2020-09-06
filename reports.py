#!/usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report():
  json_path = "/home/student-00-9f38004092b9/supplier-data/descriptions"
  rrr = ""
  report = SimpleDocTemplate("/tmp/processed.pdf")
  styles = getSampleStyleSheet()
  for i in os.listdir(json_path):
    if i.endswith("txt"):
      with open(json_path + "/" + i, 'r') as f:
        ln = f.readlines()
        rrr += "<br/> <br/> name: " +  ln[0].strip() + "<br/> weight: " + ln[1].strip()
  report_title = Paragraph("Processed Update on 9/6/2020", styles["h1"])
  report_table = Paragraph(rrr, styles["Normal"])
  report.build([report_title, report_table])

if __name__ == "__main__":
  generate_report()
