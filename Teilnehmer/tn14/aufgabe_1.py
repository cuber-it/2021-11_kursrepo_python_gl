#!/usr/bin/env/ python3
import sys
import os
import math
# Klassen: KlassenName
# Konstante: KONSTANTEN_NAME
# Funktionen: mach_was
# Variablen: meine_variable
# Wenn ein Name mit _ beginnt --> "hidden"
# Wenn ein Name mit __beginnt --> gehoert Python

eingabe=input("Eingabe: ")
print(type(eingabe))
print(eingabe)
if eingabe.isdigit():
    print("Inhalt is Ist eine Ganzzahl")
    wert=int(eingabe)
    value=wert**2
    print("Quadrat von" , wert," ist",value)
else:
    print("Inhalt ist was anderes")

