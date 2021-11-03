#!/usr/bin/env python3
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"

# Datei oeffnen und einlesen (klassische Schreibweise)
# f = open(FNAME, "r")
# text = f.read()
# f.close()

# Modernere Variante mit automatischem Schliessen der Datei, heute eher ueblich
with open(FNAME, "r") as f:
    text = f.read()

print(text[:100])

# zeilen = text.split("\n") # Zaehlt auch leere Zeilen mit
zeilen = text.splitlines() # Alternative

zeilen = zeilen[18:] # Ignoriere die ersten 18 Kommentarzeilen

while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_":
        break
    for zeile in zeilen:
        if eingabe in zeile:
            print("Alternativen:", zeile)