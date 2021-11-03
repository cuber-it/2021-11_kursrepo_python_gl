#1/usr/bin/env python3
import sys
import os

e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
  print("ist eine Ganzzahl")
  z=int(e)
  v=z ** 2
  print("Quadrat von ", z," ist", v )
elif e.isdecimal():
  print("ist auch eine Zahl")  
else:
  print("ist etwas anderes")