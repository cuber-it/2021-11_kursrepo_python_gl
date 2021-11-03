#!/usr/bin/env python3
import sys
import os
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"

with open(FNAME, "r") as f:
    text = f.read()
zeilen = text.split("\n")

while True:
    suchwort = input("Suchwort:")
    if suchwort == "_exit_":
        break
    gefunden = False
    for zeile in zeilen:
        if zeile.startswith("#"):
            continue
        worte = zeile.split(";")
        gefunden = False
        for wort in worte:
            if wort == suchwort:
                gefunden = True
                break
        if gefunden:
            print("Alternativen: \n", zeile)
    if gefunden == False:
        print("Suchwort wurde nicht gefunden")

        
