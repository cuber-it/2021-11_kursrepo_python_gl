#!/usr/bin/env python3
#Beispiel für Funktionen
import sys
import os
import random
import datetime

def read(fnames):
    collection =[]
    for fname in fnames:
        with open(fname,'r') as fd:
            #zeilen = fname.read().splitlines()
            #buchstaben = len(fname)
            collection.append({"NAME":fname, "SIZE": len(text) "TEXT":text})
    return collection     #nicht vollständig

def write(fname, data):
    with open(fname,"w") as fd:
        for file in data:
            print("-"*120, file=fd)
            print(file "NAME")
            # nicht vollständig

def archiv(out,*args):
    pass

if __name__=="__main__":
    if len(sys.argv) < 3:
        print(f"usage:{sys.argv[0]} outfile inputfile...", file=sys.stderr)
        sys.exit(1)

try:
    daten = read(sys.argv[2:])
    write(sys.argv[1], daten)
    sys.exit(0)
except Exception as e:
    print("Fehler",e)
    sys.exit(2)
