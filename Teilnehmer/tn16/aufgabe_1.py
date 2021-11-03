#!/usr/bin/env python3
import sys
import os
# Klassen: KlassenName
# Konstante: KONSTANTEN_NAME
# Funtionen: mach_was
# Variablen:  meine_daten
# Wenn ein Name mit - beginnt -" Hidden"
e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("Inhalt ist eine Ganzzahl")
    z = int(e)
    v = z ** 2
    print (" Quadrat von ", z , )