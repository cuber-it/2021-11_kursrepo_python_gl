#!/usr/bin/env python3

eingabe = input("Bitte 6 aus 49: ")
#print(f"#{eingabe}#")
werte = eingabe.split(" ")
#print(werte)

tipp = []
try:
    if len(werte) != 6:
        print("Falsche Anzahl von Werten")
        exit()
        
    for wert in werte:
        zahl = int(wert)

        if zahl < 1 or zahl > 49:
            print("Falscher Wert")
            exit()

        if zahl in tipp:
            print("Doppelter Wert")
            exit()

        tipp.append(zahl)
        print(tipp)    
except Exception as e:
    print("Fehler: ", e)
    exit()

print(f"Tipp: {tipp}")