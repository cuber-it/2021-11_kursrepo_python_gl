#!/usr/bin/env python3
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"  # r= nur lesen ohne zu bewerten

# Klassische Schreibweise für Dateiöffnen
# f = open(FNAME, "r")
# text = f.read() # ganze Datei als ein String komplett einlesen
# f.close()

# Moderne üblichere Schreibweise mit auto-close
with open(FNAME,"r") as f:
    text = f.read()

#print (text[:100])  # slice auf ersten 100 Buchstaben
#print ("Länge:", len(text))

#zeilen = text.split("\n")
zeilen = text.splitlines()

#print(zeilen[:5]) # slice auf ersten 5 Zeilen
#print ("Zeilenzahl: ", len(zeilen))

#zeilen = zeilen[18:] # erste 18 Kommentarzeilen ignorieren

# Entfernen von Kommentaren
rein_text =[]
for zeile in zeilen:
    if not zeile.startswith("#"):
        rein_text.append(zeile)

while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_":
        break
    for zeile in zeilen:
        if eingabe in zeile:
            print("Alternativen: ",zeile)
