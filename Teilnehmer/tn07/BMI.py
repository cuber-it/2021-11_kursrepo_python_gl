#!/usr/bin/env python3

fname = r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn07/BMI.csv"
with open(fname) as f:
    zeilen = f.read().splitlines()
#print(zeilen)

header = zeilen[0].replace(" ","").split(",")
daten = zeilen[1:]
personendaten = []
for person in daten:
    p = person.replace(" ","").split(",")
    personendaten.append(p)
print(header)
print(daten)
print(personendaten)

# Gewicht / ( Größe * Größe )