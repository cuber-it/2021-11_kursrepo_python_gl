#!/usr/bin/env python3
#Beispiel für Funktionen
import sys
import os
import glob

path = input("Verzeichnis:" )
pattern = input("Dateinamenmuster:")

found = glob.glob(os.path.join(path,pattern))

datei_inhalte =[]
for fname in found:
    #print(fname, os.stat(fname)[6])
    with open(fname) as fd:    # mehrere dateien einlesen
        zeilen = fd.read().splitlines() 
    datei_inhalte.append((fname, zeilen))

print(datei_inhalte)
