#!/usr/bin/env python3
import sys
import os
e = input("Bitte Ganzzahl eingeben:")
if e.isdigit():
    print("e ist eine Ganzzahl")
    z = int(e)
    v = z ** z
    print("Quadrad von ", z, " ist ", v)
else:
    print("e ist keine Zahl")



