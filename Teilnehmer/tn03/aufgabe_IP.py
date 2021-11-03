#!/usr/bin/env python3
import sys
import os

print("Auswertung von IP Adressen:")
print("#"*27)
eingabe = ""
while True:
    eingabe = input("Eingabe der IP Adresse mit optionalem Port ([exit] fuer Programmende):")
    if eingabe.lower() == "exit":
        break
    ip_split = eingabe.split(":")
    x = len(ip_split)
    print(x)
    if x < 2:
        print("Es wurde kein Port angegeben.")
    print(ip_split)