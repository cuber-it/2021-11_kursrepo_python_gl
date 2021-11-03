#! /usr/bin/env python3
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"

# Klassische Schreibweise für Dateiöffnen
#f = open(FNAME, "r")
#text = f.read() # Ganze Datei als ein String komplett eingelesen
#f.close()

# Moderne, meist üblichere Schreibweise, mit auto-close
with open(FNAME, "r") as f:
    text = f.read()

#print(text[:1000])
#print("Länge: ", len(text))

#zeilen = text.split("\n")
# Alternativ mit Methode von strings
zeilen = text.splitlines()

#print(zeilen[:5]) # slice of die ersten 5 Zeilen
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
    for zeile in zeilen:
        if eingabe in zeile:
            print("Alternativen: ", zeile)
