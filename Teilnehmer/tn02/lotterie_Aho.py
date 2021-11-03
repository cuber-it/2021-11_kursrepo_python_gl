#!/usr/bin/env python3

tipp = []
tipp = input("6 Zahlen eingeben mit Komma getrennt (1 bis 49): ")
zahlen = tipp.replace(" ","").split(",")
if len(tipp) > 5:
    print("Bitte nur 6 Zahlen")
    print(tipp)
    exit()
if len(tipp) < 6:
    print("Bitte genau 6 Zahlen eingeben")
    print(tipp)

for zahl in zahlen 
# if zahl.isnumeric()
#if not (1 <= tipp[i]<= 49)
#  exit() 
else:
    print("Eingabe ist keine Zahl")
    exit()
