#!/usr/bin/env python3
import sys
import os

eingabe=input("Bitte geben Sie sechs unterschiedliche Zahlen zwischen 1 und 49 ein: ")

zahlen=eingabe.split(",")
if len(zahlen)!=6:
    print("Anzahl der Eingabewerte nicht sechs.")
    exit()
if len(set(zahlen)) != len(zahlen):
    print("Doppelte vorhanden.")
    exit()
keineZahlen=[]
for zahl in zahlen:
    if not (zahl.isdigit() and 0<int(zahl)<50):
        keineZahlen.append(zahl)
if len(keineZahlen)>0:
    print("Bei ", *keineZahlen, " handelt es sich nicht um eine Zahl/Zahlen zwischen 1 und 49.")
    exit()
tipp=[]
for i in range (0,len(zahlen)):
    tipp.append(int(zahlen[i]))
print("Tipp", *tipp)