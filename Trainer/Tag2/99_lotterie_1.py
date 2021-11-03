#!/usr/bin/env python3
import random

ziehung = random.sample(range(1,50),k=6)
ziehung.sort()
print(ziehung)

count = 0
zahlen = []
while count < 6:
    try:
        zahl = int(input("Eine Zahl: "))
        if zahl < 1 or zahl > 49:
            print("ungültige zahl")
        elif zahl in zahlen:
            print("doppelte zahl")
        else:
            zahlen.append(zahl)
            count += 1
    except:
        print("Das war wohl nix!")

zahlen.sort()
print(zahlen)

# die Langversion
treffer = 0
for n in zahlen:
    if n in ziehung:
        treffer += 1
print("Treffer: ", treffer)

# Einzeiler :-)
treffer = len(list(set(ziehung) & set(zahlen)))
print("Treffer: ", treffer)


    