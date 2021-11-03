#!/usr/bin/env python3
   
eingabe = input("Bitte Lottozahlen eingeben:").replace(" ","")
if eingabe.find(",") < 0:
    print("Es konnten keine Komma getrennten Lottozahlen erkannt werden")
    exit()
zahlen = eingabe.split(",")
if len(zahlen) != 6:
    print("Es wurden nicht 6 Lottozahlen angegeben")
    exit()
for zahl in zahlen:
    zahl = zahl.replace(",","")
    try:
        zahl = int(zahl)
    except:
        print(zahl, "konnte nicht als Zahl erkannt werden")
        exit()
    if zahl < 1 or zahl > 49:
        print(zahl, "Liegt auserhalb des Wertebereiches für Lottozahlen")
        exit()
zahlen = list(set(zahlen))
if len(zahlen) != 6:
    print("Lottozahlen ungueltig, mindenstens eine Zahl ist doppelt")
    exit()
print("Die Lottozahlen:")
print(*zahlen)
print("sind gueltig")

    

     