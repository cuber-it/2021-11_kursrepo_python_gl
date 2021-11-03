#!/usr/bin/env python3
import sys
import os
import pprint

#d = {"Iterator":["Datum","Lost","High","Volume"]}

#apple_stock = [{Datum:}]
import pandas 
#d = pandas.read_csv("/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv").to_dict('records')
#print(d[0])

FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"

with open(FNAME) as fd:
    zeilen = fd.read().splitlines()

header = zeilen[0].replace(" ", "").split(",")
daten = []

for zeile in zeilen[1:]:
    if zeile.strip() !="":
        zeile = zeile.replace(" ", "").replace("$", "")
        einzelwert = {}
       #for i in range(0, len(header)):
        for i, key in enumerate(header):
            if "." in zeile[i]:
                zeile[i] = float(zeile[i])
            elif zeile[i].isdigit():
                zeile[i] = int(zeile[i])

            # eintragen im Dict
            einzelwert[key] = zeile[i] 
        daten.append(einzelwert)
print(daten)