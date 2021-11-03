#!/usr/bin/env python3
#Beispiel für Funktionen
import sys
import os

def bmi_rechner(gewicht=1, groesse=1):
    bmi = gewicht/(groesse**2)
    return bmi


eingabe = int(input("Bitte eingeben  Körpergewicht (kg): , Grösse (m) "))
print(eingabe)
x =bmi_rechner(eingabe)
if bmi < 18.5 :
    print("Untergewicht!")
elif bmi > 18.5 or < 24.9 :
    print("Normalgewicht")
elif bmi > 30 or < 34.9 :
    print("Starkes Übergewicht")
elif bmi > 35 or < 39.9 :
    print("Adipositas II")
elif bmi > 40 :
    print("Adipositas III")
