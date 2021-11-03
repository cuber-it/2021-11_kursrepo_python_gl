#!/usr/bin/env/ python3
import sys
import os

#Eingabe
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt" # groß weil Kosntante
#Klassich oeffnen
f=open(FNAME,"r")
text=f.read() # Datei als ein String einlesen
f.close()
#moderner und kuerzer und mit autoclose!!!
with open(FNAME,"r") as f:
    text2=f.read()

print(len(text))
print(len(text2))

# Aufteilung in Zeilen
zeilen=text2.split("\n") # splitzeichen ist Zeilenumbruch
print("Zeilen klassisch",len(zeilen))
zeilen2=text2.splitlines()
print("Zeilen modern",len(zeilen2))
print(zeilen2[:10])
# Entfernung der Kommentarzeilen
zeilen2=zeilen2[18:]

# Suchanfrage
while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_":
        break
    for zeile in zeilen2:
        if eingabe in zeile:
            print("Alternativen: ",zeile)