#!/usr/bin/env python3
import sys
import os

print("Lotterie zum Glueck")
print("*" * 25)
while True:
    tipp = []
    eingabe = ""
    eingabe = input("Eingabe von 6 Zahlen (1 - 49, Zahlen durch ',' getrennt, 'exit' zum Beenden): ")
    if eingabe.lower() == "exit":
        break
    # Leerzeichen aus Eingabestring entfernen und die durch Komma getrennten Werte in eine Liste schreiben
    tipp = eingabe.replace(" ", "").split(",")
    # Abbruch, wenn es nicht 6 Werte sind
    if len(tipp) != 6:
        print("Fehler! Bitte genau 6 Zahlen eingeben.")
        break
    
    for zahl in tipp:
        if not zahl.isdigit():
            print("Fehler! Bitte nur Zahlen eingeben.")
            break
        elif not 1 <= int(zahl) <= 49:
            print("Fehler! Bitte nur Zahlen von 1 - 49.")
            break