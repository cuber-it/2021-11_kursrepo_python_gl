#! /usr/bin/env python3
import sys
import os

#if len(sys.argv) != 5:
#    print(f"usage {sys.argv[0]} py-InFile py-OutFile pattern replacement", file = sys.stderr)
#    sys.exit(1)

def read():
    with open(sys.argv[1]) as f:
        text = f.read()
    return text

def replacer(old_text):
    neu_text = old_text.replace(sys.argv[3], sys.argv[4])
    return neu_text

try:
    # Eingabe
    text = read()

    # Verarbeitung
    neu_text = replacer(text)

    # Ausgabe

    
    sys.exit(0)
except Exception as e:
    print("FEHLER :", e, file = sys.stderr)
    sys.exit(2)