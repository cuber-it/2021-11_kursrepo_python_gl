import sys
import os

par = {}

par["Name"] = None
par["Alter"] = None
par["Größe"] = None
par["Geschlecht"] = None

FNAME = r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn06/bmidata.csv"

with open(FNAME, "r") as f:
    text = f.read()
print(text)
textkorr = text.replace(" ","")
print(textkorr)
zeilen=textkorr.splitlines()
print(zeilen)