#!/usr/bin/env python3
import sys
import os

print("Ganzzahlrechner.")
zahl_1 = input("Eingabe Zahl 1: ")
if zahl_1.isdecimal():
    zahl_2 = input("Eingabe Zahl 2: ")
    if zahl_2.isdecimal():
        opcode = input("Eingabe der Operation [add, sub, mul, div]: ")
        if (opcode != "add") and (opcode != "sub") and (opcode != "mul") and (opcode != "div"):
            print("Das war falsch. Ende des Programms")
        else:
            if opcode == "add":
                ergebnis = int(zahl_1) + int(zahl_2)
            elif opcode == "sub":
                ergebnis = int(zahl_1) - int(zahl_2)
            elif opcode == "mul":
                ergebnis = int(zahl_1) * int(zahl_2)
            elif opcode == "div":
                ergebnis = int(zahl_1) % int(zahl_2)
            print("Das Ergebnis ist:", ergebnis)

    else:
        print("Das war falsch. Ende des Programms.")
else:
    print("Das war falsch. Ende des Programms.")