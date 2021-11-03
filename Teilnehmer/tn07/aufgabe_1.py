#!/usr/bin/env python3
import sys
import os

# Klassen: KlassenName
# Konstante: KONSTANTEN_NAME
# Funktionen: mach_was
# Variablen: meine_daten
# Wenn ein Name mit _ beginnt -> "Hidden"
# Wenn ein Name mit __ beginnt und endet -> gehört der Name python

e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("Inhalt ist eine Ganzzahl")
    z = int(e)
    v = z ** 2
    print("Quadrat von ", z, " ist", v)
else:
    print("Inhalt was anderes")




