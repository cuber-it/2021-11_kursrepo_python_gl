#!/usr/bin/env python3
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"

# Klassische Schreibweise für Dateiöffnen
#f = open(FNAME, "r")
#text = f.read() # Ganze Datei als als ein String komplett eingelesen
#f.close()

# Moderne meist üblichere Schreibweise, mit auto-close
with open(FNAME, "r") as f:
    text = f.read()

#print(text[:100]) # slice auf die ersten 100 buchstaben
#print("Länge: ", len(text))

#zeilen = text.split("\n")
zeilen = text.splitlines()

#print(zeilen[:5]) # slice auf die erssten 5 zeilen
#print("Zeilenzahl: ", len(zeilen))

#zeilen = zeilen[18:] # ignoriere die ersten 18 Kommentarzeilen

# Entfernen von Kommentaren
rein_text = []
for zeile in zeilen:
    if not zeile.startswith("#"):
        rein_text.append(zeile)


while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_":
        break
    for zeile in rein_text:
        if eingabe in zeile:
            print("Alternativen: ", zeile)
