#!/usr/bin/env python3
import sys
import os

e = input("Eingabe von 1. Zahl: ")
if e.isdigit():
    zahl_a = int(e)
else:
    print("Dies war keine Zahl, somit Unsinn und das Programm wird beendet!")
    exit()
e = input("Eingabe von 2. Zahl: ")
if e.isdigit():
    zahl_b = int(e)
else:
    print("Dies war keine Zahl und somit Unsinn!")
    exit()
op = input("Op-Code angeben (erlaubt: add; sub; mul; div; gdiv)")
if op == "add":
    ergebnis = zahl_a + zahl_b
    print("Das Ergebnis von ", zahl_a, " + ", zahl_b ,"lautet: ", ergebnis)
elif op == "sub":
    ergebnis = zahl_a - zahl_b
    print("Das Ergebnis von ", zahl_a, " - ", zahl_b ,"lautet: ", ergebnis)
elif op == "mul":
    ergebnis = zahl_a * zahl_b
    print("Das Ergebnis von ", zahl_a, " * ", zahl_b ,"lautet: ", ergebnis)
elif op == "div":
    ergebnis = zahl_a / zahl_b
    print("Das Ergebnis von ", zahl_a, " / ", zahl_b ,"lautet: ", ergebnis)
elif op == "gdiv":
    ergebnis = zahl_a // zahl_b
    rest = zahl_a % zahl_b
    print("Das Ergebnis von ", zahl_a, " // ", zahl_b ," mit Restwert lautet: ", ergebnis, "Rest ", rest)
else:
    print("Die EIngabe des op ist Unsinn!")

