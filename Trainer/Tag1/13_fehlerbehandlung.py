#!/usr/bin/env python3
summe = 0.0

while True:
    eingabe = input("Eine Zahl: ")
    if eingabe == "EXIT":
        break

    try:
        summe += float(eingabe)
    except ValueError:
        print(f"Ungültige Eingabe {eingabe}")
    finally:
        print("Weiter gehts es ...")

print(f"Gesamtsumme: {summe:.5f}")
