#!/usr/bin/env python3

eingabe = input("Bitte 6 aus 49: ")
werte = eingabe.split(" ")

try:
    if len(werte) != 6:
        raise Exception(f"Falsche Anzahl: {eingabe}")
    zahlen = []
    for n in werte:
        zahl = int(n)
        if zahl < 1 or zahl > 49:
            raise Exception(f"Falscher Wert: {n}")
        if zahl in zahlen:
            raise Exception(f"Doppelter Wert: {n}")
        zahlen.append(zahl)
    #print("Valide Zahlen: ", sorted(zahlen))
    zahlen.sort()
    print("Valide Zahlen: ", zahlen)
except ValueError as e:
    print("Fehler: ungültige Eingabe", n)
except Exception as e:
    print("Fehler: ", e)
