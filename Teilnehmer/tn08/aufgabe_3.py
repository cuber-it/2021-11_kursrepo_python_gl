#!/usr/bin/env python3
import sys
import os

while(True):
    eingabe = input("Bitte IP-Adresse eingeben:")
    if(eingabe == "exit"):
        break
    
    tripletts = eingabe.split(".")
    
    port = ""
    if(":" in tripletts[-1]):        
        port = tripletts[-1][tripletts[-1].index(":")+1:]
        tripletts[-1] = tripletts[-1][:tripletts[-1].index(":")]
    
    loopback = False
    if(eingabe.startswith("127.0.0.1")):
        loopback = True

    for triplett in tripletts:
        if("." in triplett ):
            triplett = triplett[triplett.index("."):]

    #ausgabe
    print("Die eingegebene IP-Adresse lautet:")
    print(eingabe)
    if(loopback):
        print("Es handelt sich dabei die um die Loopback-Adresse.")
    else:    
        print("Die Loopback-Adresse wurde nicht erkannt.")
    print("Die Tripletts:")
    for a in tripletts:
        print(a)
    if(port != ""):
        print("Der Port lautet:")
        print(port)
    else:
        print("ein Port wurde nicht angegeben.")

