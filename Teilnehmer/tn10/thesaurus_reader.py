#!/usr/bin/env python3
import sys
import os

FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"

# Klassische Schreibweise für Dateiöffnen
#f = open(FNAME, "r")
#text = f.read() # Ganze Datei eingelesen
#f.close()

#print(text[:100])
#print("Länge: ", len(text))

# Moderne Version, mit auto-close
with open(FNAME, "r") as f:
    text = f.read()

print(text[:5]) # Slice af 100 Buchstaben
print("Länge: ", len(text))

zeilen = text.splitlines()
print(zeilen[:5])
#print("Zeilenzahl: ", len(zeilen))

# Entfernen von Kooentaren
rein_text = []
for zeile in zeilen:
    if not zeile.startwith('#'):
        rein_text.append(zeile)

#zeilen = zeilen[18:] #ignoriere die ersten 18 kommenare
while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_":
        break
    for zeile in zeilen[18:]: #ignoriere die 18 Kommentarzeilem
        if eingabe in zeile:
            print("Alternativen: ", zeile)