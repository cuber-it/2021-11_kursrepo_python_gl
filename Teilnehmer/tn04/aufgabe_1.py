#!/usr/bin/env python3   
#das hash-bang dingen braucht man eigentlich nur für linux, darum auch python3, weil bei windows bräuchte man nur python

import sys #laufzeit sachen
import os #operating system sachen, passt auf alle betriebssysteme

# Klassen: KassenName
# Konstante: KONSTANTEN_NAME
# Funktionen: mach_was
# Variable: meine_daten
# "Hidden": _something
# pythoneigene dinge: __something__

e= input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("ist eine Ganzzahl")
    z=int(e)
    v=z*z
    print("Quadrat von" , z, "ist", v)
else:
    print("Inhalt ist was anderes")
# isdigit und Co schaut nach ob der String aus Zahlen besteht!


'''elif e.isnumeric():
    print("ist auch eine Zahl")
elif e.isdecimal():
    print("ist auch eine Zahl")'''


