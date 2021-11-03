#!/usr/bin/env python3
with open(r"/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv") as f:
  zeilen = f.read().splitlines()

header = zeilen[0].replace(" ", "").split(",")
daten = []
for zeile in zeilen[1:]:
    worte = zeile.replace(" ", "").split(",")
    for i in range(0,len(worte)):
        if worte[i].startswith("$"):
            worte[i] = float(worte[i].replace("$", ""))
        daten.append(worte)

#print(daten)

