#!/usr/bin/env python3
import sys

print("Kommandozeile: ", sys.argv)

for fname in sys.argv[1:]:
    print("Datei ", fname)
    with open(fname) as f:
        zeilen = f.read().splitlines()
        for i, zeile in enumerate(zeilen, start=1):
            print(i, zeile)
    print("-"*80)