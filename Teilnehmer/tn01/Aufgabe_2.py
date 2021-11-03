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

Eingabe1 = input("Eingabe: Zahl1 ")
Eingabe2 = input("Eingabe: Zahl2 ")
Eingabe3 = input("Eingabe: Operation ")

if Eingabe1.isdigit():
    Zahl1= Eingabe1
else:
    print("Zahl eingeben") 
    exit()
if Eingabe2.isdigit():
   Zahl2= Eingabe2 
else:
    print("Zahl eingeben") 
    exit()

if Eingabe3 == "add":
   print (int(Zahl1) + int(Zahl2))
elif Eingabe3 == "sub":
      print (int(Zahl1) - int(Zahl2)) 
elif Eingabe3 == "mul":
      print (int(Zahl1) * int(Zahl2))
elif Eingabe3 == "div":
      print (int(Zahl1) / int(Zahl2))
else:                  
    print("Operator eingeben: ")

