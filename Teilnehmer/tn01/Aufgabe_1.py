#!/usr/bin/env python3
import sys
import os
import math

#Klassen: KlassenName
#Konstante: Konstanten_Name
#Variablen: meine_daten
#Funktion: mach_was
#Wenn ein Name mit _ beginnt -> "Hidden"
#Wenn ein Name mit __beginnt und endet -> gehoert der Name Python

e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("Inhalt ist eine Zahl")  
    z= int(e)
    v= z*z
    print("Quadrat von",z," ist ",v)
else:
    print("Inhalt ist was anderes")    



