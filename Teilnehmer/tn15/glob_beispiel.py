#! /usr/bin/env python3
import os
import glob

# path = input("Verzeichnis: ")
# pattern = input("Dateinamenmuster: ")

path = r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn15"
pattern = r"*.py"

found = glob.glob(os.path.join(path, pattern)) # path join setzt automatisch die korrekte Filetrennung je nach OS um

datei_inhalte = []
for fname in found:
    # print(fname, os.stat(fname))
    with open(fname) as fd:
        zeilen = fd.read().splitlines()
    datei_inhalte.append((fname, zeilen))

print(datei_inhalte)