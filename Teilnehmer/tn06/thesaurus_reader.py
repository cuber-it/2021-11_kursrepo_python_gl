#!/usr/bin/env python3
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt" # r steht für raw, Daten werden nicht verändert

# Klassische Schreibweise um Dateinen zu öffen
#f = open(FNAME,"r") #"r" steht für read
#text = f.read()
#f.close()

# Moderne Schreibweise, mit auto-close
with open(FNAME, "r") as f:
    text = f.read()

#print(text[:100]) # Gibt die ersten 100 Zeichen aus.. slice auf ersten hundert Buchstaben
#print("Länge: ", len(text))

#zeilen = text.split("\n") äquivalent zum Unteren
zeilen = text.splitlines()
#print(zeilen[:5]) # slice auf die ersten 5 Zeilen
#print("Zeilenzahl: ", len(zeilen))

# Entfernen von Kommentaren
#rein_text = []
#for zeile in zeilen:
#    if not zeile.startswith("#"):
#        rein_text.append(zeile)
zeilen = zeilen[18:] # ignoriere die ersten 18 Zeilen
while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_":
        break
    for zeile in zeilen: 
        if eingabe in zeile:
            print("Alternativen: ", zeile)