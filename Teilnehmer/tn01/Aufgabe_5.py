#!/usr/bin/env python3
import sys
import os
import math

Eingabe = input("Bitte 6 Ziffern mit Komma getrennt eingeben: ")

EingabeListe = Eingabe.split(",")
anzahl = len(EingabeListe)
if anzahl == 6:  
   print("Anzahl = 6")
else:   
   print(" falsche Anzalh")
   exit()

tipp=[]
for i in range(0,anzahl):
    if EingabeListe[i].isdigit:
       print(EingabeListe[i])
    else:  
       print("Keine Zahl")
       exit()

    if not (0< int( EingabeListe[i]) <= 49):
       print(" Falscher Zahlenbereich") 
       exit() 
    tipp.append(EingabeListe[i])   
next       

Liste_Set= set(EingabeListe)
if len(Liste_Set) != 6:
   print(" Doppelte") 
   exit() 

print ("Tipp : " , tipp )