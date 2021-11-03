#!/usr/bin/env python 3
import sys
import os

# Bezeichnungskonventionen
# Klassen: KlassenName
# Konstante: KONSTANTEN_NAME
# Funktionen: mach_was
# Variablen: meine_daten
# Wenn ein Name mit _ beginnt -> "Hidden"
# Wenn ein Name mit __ beginnt und endet -> Name gehoert Python

e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("Eingabe ist eine Ganzzahl.")
    z = int(e)
    v = z * z
    print("Quadrat von", z, "ist", v)
else:
    print("Eingabe ist was anderes.")