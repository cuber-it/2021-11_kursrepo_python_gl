#! /usr/bin/env python3

import sys
import os
import pprint

# Beispiel dictionary mit Ausgabe
#datei_dict = {"Datei_Name": 
#    {
#        "Wörter": 89,
#        "Zeilen": 13,
#        "Inhalt": "Lipsum"
#    }
#}
#pprint.pprint(datei_dict)
#print(datei_dict.get("Datei_Name").get("Wörter"))

#fnames = [
#    r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn15/ip_tester.py",
#    r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn15/apple_stocks.py"
#    ]
#fname_out = r"out.txt"

#if __name__ == "__main__":
#    if len(sys.argv) < 3:
#        print(f"usage: {sys.argv[0]} outfile inputfile ...", file = sys.stderr)

# Dictionary an Listen anhängen
def read(fnames):
    collection = []
    for fname in fnames:
        with open(fname) as f_in:
            inhalt = f_in.read()
            collection.append({
                "NAME": fname,
                "SIZE": len(inhalt),
                "TEXT": inhalt
            })
    return collection


def write (fname, data):
    with open(fname, "w") as fd:
        for file in data:
            print("-"*120, file = fd)
            print(file["NAME"], file["SIZE"], file = fd)
            print("-"*120, file = fd)
            print(file["TEXT"], file = fd)
            print("="*120, file = fd)


Lösung mit reinem Dictionary
def readDict(fnames):
   fileDict = {}
   for fname in fnames:
       with open(fname) as f_in:
           inhalt = f_in.read()
           fileDict[fname] = {
               "Wörter": len(inhalt),
               "Inhalt": inhalt                
           }
   return readDict


def writeDict(fname, data):
   with open(fname, "w") as fd:
       for key in data.keys():
           print(data.key["NAME"], file["SIZE"], file = fd)
           print("-"*120, data.get(key).get(Wörter), file = fd)
           print("-"*120, file = fd)
           print(file["TEXT"], file = fd)
           print("="*120, file = fd)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} outfile inputfile ...", file = sys.stderr)
        sys.exit(1)
    try:
        # Listen Lösung
        #daten = read(sys.argv[2:])
        #write(sys.argv[1], daten)
        #sys.exit(0)

        # Dictionary Lösung
        daten = readDict(sys.argv[2:])
        type(daten)
        writeDict(sys.argv[1], daten)
        sys.exit(0)
    except Exception as e:
        print("Fehler: ", e)
        sys.exit(2)