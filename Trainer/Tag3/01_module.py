#!/usr/bin/env python3

print(dir())
import sys
import os, os.path

print(dir())
print("-" * 80)
print(dir(sys))

print("-"*80)
print(sys.path) # der Suchpfad für Module first come - first serve

# Suchpfad entweder direkt mit Listenmethoden manipulieren
# oder mit PYTHONPATH ergänzen

print("-" * 80)
from os.path import join# joint Pfadnamen, hat nichts mit den Strings zu tun!
print(join("a", "b", "c"))

#def join(*args):
#    print("Mein eigenes Join")
#print(join("a", "b", "c")) # bei Funktion gilt: der letzte gewinnt


