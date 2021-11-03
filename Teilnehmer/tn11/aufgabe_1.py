#!/usr/bin/env python3
import sys
import os

# Klassen: KlassenName
# Konstante: KONSTANTEN_NAME
# Funktionen: mach_was
# Variablen: meine_daten
# Wenn ein Name mit _ beginnt, dann heißt das  -> "Hidden"
# Wenn ein Name mit __ beginnt und endet, dann gehört der Name Python
e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("Inhalt ist eine ganze Zahl")
    z = int(e)
    v=z*z
    print("Quadrat von ",z," ist ",v)
#elif e.isnumeric():
#    print("Inhalt ist auch eine Zahl")
#elif e.isdecimal():
#    print("Inhalt ist auch eine Dezimalzahl")
else:
    print("Inhalt ist was anderes")


