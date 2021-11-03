#!/usr/bin/env/ python3
import sys
import os



while eingabe !="q":
    eingabe = input("Bitte 6 Zahlen eingeben (mit Komma getrennt) (q=Exit): ").replace(" ","").split(",")
    if len(eingabe) != 6:
        print("Das sind keine 6 Zahlen")
        print("Das sind ",len(eingabe)," Zahlen")
        break
    tipp=[]
#print(len(eingabe))
    print(eingabe)
    for zahl in eingabe:
        if zahl.isdigit():
            wert=int(zahl)
            if not (1 <= wert <= 49):
                print("Zahl",zahl," nicht zwischen 1 - 49")
                exit()
            tipp.append(wert)
            if len(set(tipp)) != len(tipp):
                print("Doppelte Werte")
                exit()
    print("der Tipp war",*tipp)
exit()
    