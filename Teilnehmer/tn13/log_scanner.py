#!/usr/bin/env python3
fname = r"/home/coder/Workspace/aktueller-kurs/Materialien/sample.log.txt"

fd=open(fname,'r')
text=fd.readlines()
fd.close()

for zeile in text:
    if "TRACE" in zeile:
        print(f"{zeile[6:14]}")