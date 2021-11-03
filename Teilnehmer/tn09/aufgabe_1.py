#!/usr/bin/env python3
import sys
import os



e = input("Eingabe: ")
print(type(e))
print(e)
if e.isdigit():
    print("ist eine Zahl")
else:
    print("Inhalt ist was anderes")