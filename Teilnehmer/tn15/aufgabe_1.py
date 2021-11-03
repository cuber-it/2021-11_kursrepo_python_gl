#!/usr/bin/env python3
import sys
import os

# Konventionen
# Klassen: KlassenName
# Konstante: KONSTANTEN_MAME
# Funktionen: mach_was
# Variablen: meine_daten
# Wenn ein Name mit _ beginnt -> "Hidden"
# Wenn ein Name mit __ beginnt und endet -> gehört der Name python

e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("Inhalt ist eine Zahl")
    z = int(e)
    v = z * z
    print("Quadrat von", z, "ist", v)
elif e.isnumeric():
    print("Inhalt ist auch eine Zahl")
elif e.isdecimal():
    print("Inhalt ist auch eine Zahl")
else:
    print("Inhalt ist etwas anderes")
