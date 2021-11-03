#!/usr/bin/env python3
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"

with open(FNAME) as fd:
    zeilen = fd.read().splitlines()

header = zeilen[0].replace(" ","").split(";")
daten = {}

for zeile in zeilen[1:]:
    if zeile.strip() != "":
       zeile = zeile.replace(" ","").replace("$","").split(",")
       einzelwert = {
          header[1]: zeile[1],
          header[2]: zeile[2],
          header[3]: zeile[3],
          header[4]: zeile[4]
        }

       # daten{zeile[0]} = einzelwert    

    #print(daten)            
#pprint.pprint(daten)
#print("")