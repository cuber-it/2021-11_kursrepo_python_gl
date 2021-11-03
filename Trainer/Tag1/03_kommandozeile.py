#!/usr/bin/env python3
import os
import sys

print("Inhalt des Environment:")
print(os.environ) # Dict
print("-"*80)
print("PATH", os.environ["PATH"]) # Element aus dem Dict = String
print("-"*80)
print("Aufruf aus der Kommandozeile: ", sys.argv) # Liste
print("-"*80)
print("Aufruf aus der Kommandozeile: ", sys.argv[0]) # 1. Element der Liste = String = Programmname
