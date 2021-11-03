#!/usr/bin/env python3

eingabe = ""
eingabe = input("Lotterie-Tipp (1-49) bitte mit Komma eingeben: (x,x,x,x,x,x)\n")

zahlen = eingabe.split(",")
liste = []
anz_zahlen = len(zahlen)
if anz_zahlen < 6 or anz_zahlen > 6:
    print("Ungültige Anzahl an Zahlen.")
    exit()
else:
    for zahl in zahlen:
        if zahl.isnumeric():
            zahl = int(zahl)
            if zahl < 1 or zahl > 49:
                print(f"Die Zahl {zahl} ist ungültig.")
                exit()    
            liste.append(zahl)
        else:
            print(f"{zahl} ist keine Zahl.")
            exit()

if len(set(liste)) < 6:
    print("Ungültige Eingabe! Es gibt doppelte Zahlen.")
    exit()
else:
    print("Ihr abgegebener Tipp ist gültig und lautet: ", *liste)    


