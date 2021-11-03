#!/usr/bin/env python3
import os
import sys

erg = None
a = input("Bitte erste Ganzzahl eingeben:")
if a.isdigit:
    b = input("Bitte zweite Ganzzahl eingeben:")
    if b.isdigit:
        a = int(a)
        b = int(b)
        operant = input("Bitte add, sub, mul oder div als Operant waehlen:")
        if operant == "add":
            erg = a + b 
            print("Das Ergibnis von ", a, "+", b, " ist", erg )
        elif operant == "sub":
            erg = a - b 
            print("Das Ergibnis von ", a, "-", b, " ist", erg )
        elif operant == "mul" and b != 0:
            erg = a * b 
            print("Das Ergibnis von ", a, "*", b, " ist", erg )
        elif operant == "div":
            erg = a // b
            rest = a % b
            print("Das Ergibnis von ", a, "/", b, " ist", erg, " Rest:", rest)

if erg == None:
    print("Das ist Quatsch!")

