#!/usr/bin/env python3
import os
import glob

path = input("Verzeichnis: ")
pattern = input("Dateinamenmuster: ")

found = glob.glob(f"{path}/{pattern}")

datei_inhalte = []
for fname in found:
    # print(fname, os.stat(fname)[6])
    with open(fname) as fd:
        zeilen = fd.read().splitlines()
    datei_inhalte.append((fname, zeilen))

print(datei_inhalte)
