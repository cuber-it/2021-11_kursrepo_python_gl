#!/usr/bin/env python3
import sys
import os

# Klassen: KlassenNamen
# Konstante: KONSTANTE_NAME
# Funktionen: mach_was
# Variablen: meine_daten
# Wenn ein Name mit _beginn -> "Hidden"
# Wenn ein Name mit __beginnt und endet -> gehört der Name python

e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("Inhalt ist eine Zahl")
    z = int(e)
    v = z*z
    print("Quadrat von", z,"ist ", v)
else:
    print("Inhalt was anderes")


