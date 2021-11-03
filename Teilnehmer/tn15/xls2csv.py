#! /usr/bin/env python3
import pandas
import sys

#FNAME = r"home/coder/Workspace/aktueller-kurs/Materialien/Verkaufsdaten.xlsx"
if len(sys.argv) != 3:
    print(f"usage: {sys.argv[0]} Source.xls Target.csv", file = sys.stderr)
    sys.exit(1)
try:
    pandas.read_exceö(sys.argv[1]).to_csv(sys.argv[2], index = None, header = True)
    sys.exit(0)
except Exception as e:
    print("FEHLER", e)
    sys.exit(2)