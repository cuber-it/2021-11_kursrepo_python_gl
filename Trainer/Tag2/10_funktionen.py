#!/usr/bin/env python3
def eingabe():
    return input("Eingabe:")

def verarbeitung(wert, daten):
    return int(wert) + int(daten)

def ausgabe(wert):
    print("Ausgabe:", wert)

daten = eingabe()
ergebnis = verarbeitung(4711, daten)
ausgabe(ergebnis)   