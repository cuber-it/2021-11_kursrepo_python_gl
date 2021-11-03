#!/usr/bin/env python3
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"

#Klassische Schreibweise für Dateiöffnen
#f = open(FNAME,"r")
#text = f.read() # Ganze Datei als ein String komplett eingelesen
#f.close()
#

#Moderne meist üblichere Schreibweise, mit auto-close
with open(FNAME, "r") as f:
    text = f.read()

#print(text[:100])
#print("Länge: ", len(text))

#zeilen = text.split("\n")
zeilen = text.splitlines()

#print(zeilen[:5]) # slice auf die ersten 5 zeieln
#print("Zeilenzahl: " , len(zeilen))

while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_":
        break
    for zeile in zeilen[18:]: #ignoriere die ersten 18 Kommentare
        if eingabe in zeile:
            print("Alternativen: ", zeile)

