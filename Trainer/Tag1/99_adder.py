#!/usr/bin/env python3
summe = 0.0

while True:
    eingabe = input("Eine Zahl: ")
    if eingabe == "EXIT":
        break

    # ein wirklich schmutziger kleiner Trick :-)
    # zur Fehlervermeidung
    if eingabe.replace('.', '', 1).isdigit():
        summe += float(eingabe)
    else:
        print(f"Ungültige Eingabe {eingabe}")

print(f"Gesamtsumme: {summe:.5f}")