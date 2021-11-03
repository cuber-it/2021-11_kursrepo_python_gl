#!/usr/bin/env python3
import sys
import os
import random
import glob

path = input("Verzeichnis: ")
pattern = input("Dateinamenmuster: ")

found = glob.glob(os.path.join(path, pattern))
datei_inhalte = []
for fname in found:
    # print(fname, os.stat(fname)[6])
    with open(fname) as fd:
        zeilen = fd.read().splitlines()
    datei_inhalte.append((fname, zeilen))

print(datei_inhalte)



# def readdata_stats(filename):
#     collection = []
#     for name in filename:
#         with open(name) as f:
#             inhalt = f.read() # einlesen als gesamtstring
#             n_character = len(inhalt) # Zaehle die Zeichen
#             collection.append({"Name":name,"Size":n_character,"Inhalt":inhalt})
            
#     return(n_character)

# f_name="/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn14/aufgabe_1.py"
# print(f_name)
# check=readdata_stats(f_name)

#print(check)


