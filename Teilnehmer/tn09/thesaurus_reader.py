#!/usr/bin/env python3
import sys
import os

file_path = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"

# # Klassische Variante Datei öffnen
# f = open(file_path, "r")
# text = f.read()  # Ganze Datei eingelesen
# f.close()

# Moderne meist übliche Methode mit auto-close
with open(file_path, "r") as f:
    text = f.read


#zeilen  = text.split("\n")
text_raw = text.splitlines()
file_lines = len(text_raw)


while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_"
        break
    for zeile in zeilen:
        if eingabe in zeile:
            print("Alternativen", zeile)