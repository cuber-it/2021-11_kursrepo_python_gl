#!/usr/bin/env python3
"""
Einfache BMI Rechner

Eingaben: Körpergewicht in Kilo und Grösse in Metern
Berechnung: BMI-Wert: Körpergewicht geteilt durch die Körpergröße in Metern zum Quadrat
Ausgabe: Ein Hinweis, s.u

Untergewicht: BMI < 18,5
Normalgewicht: BMI 18,5-24,9
Übergewicht: BMI 25-29,9
Starkes Übergewicht (Adipositas Grad I): BMI 30-34,9
Adipositas Grad II: BMI 35-39,9
Adipositas Grad III: BMI > 40
"""
import sys

if len(sys.argv) != 3:
    gewicht = input("Gewicht in kg: ")
    groesse = input("Grösse in m: ")
else:
    groesse = sys.argv[1]
    gewicht = sys.argv[2]


bmi = float(gewicht) / (float(groesse) ** 2)

print("Der BMI ist: ", bmi)

if bmi < 18.5:
    print("Untergewicht")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normalgewicht")
elif bmi >= 24.9 and bmi < 29.9:
    print("Übergewicht")
else:
    print("Keine Schoki heute abend!!!")
