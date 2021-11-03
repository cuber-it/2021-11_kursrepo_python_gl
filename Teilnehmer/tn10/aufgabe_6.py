#!/usr/bin/env python3
import os
import glob

path = input("Verzeichnis: ")
pattern = input("Dateinamemuster: ")

#found = glob.glob(os.path.join(path, pattern))
found = glob.glob(f"{path}/{pattern}")

datei_inhalte = []
for fname in found:
  #  print(fname)
  #  print(fname, os.stat())
    with open(fname) as fd:
        zeilen = fd.read().splitlines()
    datei_inhalte.append(fname, zeilen)

print(datei_inhalte)


# Verzeichnis: /home/coder/Workspace/aktueller-kurs/Teilnehmer/tn10
# *py