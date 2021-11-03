#!/usr/bin/env python3
import random

eingabe = "1, 2, 3, 4, 5, 6"
#zahlen = "1, 2, 3, 4, 500, 6"
#zahlen = "1, 2, 3, 4, 6"
#zahlen = "1, 2, 3, 4, 4, 6"
#zahlen = "1, 2, 3, 4, -5, 6"
#zahlen = "1, 2, 3, 4, A, 6"

#eingabe = input("6 Zahlen zwischen 1 und 49: ")
zahlen = eingabe.replace(" ", "").split(",")

if len(zahlen) != 6:
    print("Länge stimmt nicht ", zahlen)
    exit()

tipp = []
for zahl in zahlen:
    if not zahl.isdigit():
        print("Keine Zahl: ", zahl)
        exit()
    zahl = int(zahl)    
    if not (1 <= zahl <= 49):
        print("Nicht gültig: ", zahl)
        exit()
    tipp.append(zahl)

if len(set(tipp)) != 6:
    print("Doppelte!")
    exit()

print("Ihr Tipp :", *tipp)

ziehung = random.sample(range(1,49), 6)
print("Ziehung: ", *ziehung)
treffer = list(set(tipp).intersection(set(ziehung)))
print("Treffer: ", *treffer)







# if not (1 <= eingabe[i] <= 49):
#    exit()     
#
# for i in range(0, len(zahlen)):
#     if not zahlen[i] ...:
#        exit()
#
# oder:
#
# i = 0
# while i < len(zahlen):
#    if not zahlen[i] ...:
#        exit()
#    i = i + 1