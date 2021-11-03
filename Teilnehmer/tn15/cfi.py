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

zahl1 = input("1. Zahl: ")
zahl2 = input("2. Zahl: ")
op_code = input("Operation: ")

if zahl1.isdigit() and zahl2.isdigit():
    print("beides Zahlen")
    zahl1 = int(zahl1)
    zahl2 = int(zahl2)
    if op_code == "add":
        erg = zahl1 + zahl2
    elif op_code == "sub":
        erg = zahl1 - zahl2
    elif op_code == "mul":
        erg = zahl1 * zahl2
    elif op_code == "div":
        erg = zahl1 / zahl2
    elif op_code == "g_div":
        erg = str(zahl1 // zahl2) + " Rest " + str(zahl1 % zahl2)
    else:
        erg = "Undefinierte Operation"
    print(erg)
else:
    print("keine Zahlen")