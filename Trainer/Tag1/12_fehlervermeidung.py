#!/usr/bin/env python3
eingabe = input("Eine Ganzzahl zwischen 0 und 50: ")

if eingabe.isdigit() and int(eingabe) >= 0 and int(eingabe) <= 50: # Reihenfolgt ist wichtig! short circuit Evaluation, erstes False beendet Auswertumg
    print(f"Es ist eine Ganzzahl {int(eingabe)}")
else:
    print(f"Ungültige Eingabe {eingabe}")

# oder mit einer Assertion
assert eingabe.isdigit() and int(eingabe) >= 0 and int(eingabe) <= 50, "Ungültige Eingabe"