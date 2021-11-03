#!/usr/bin/env python3
import sys
import os

e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("Inhalt ist eine Ganzzahl")
    z = int(e)
    v = z * z
    print("Quadrat von ", z , " ist ", v)
else:
    print("Inhalt is was anderes")

