#!/usr/bin/env python3
import os
import glob

path = input("Verzeichnis: ")
pattern = input("Dateinamenmuster: ")

found = glob.glob(f"{path}/{pattern}")

for fname in found:
    print(fname, os.stat(fname)[6])