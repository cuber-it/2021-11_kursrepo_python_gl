#!/usr/bin/env python3
import sys
import os


def check():
    if len(sys.argv) != 5:
        print(f"usage {sys.argv[0]} py-InFile py-OutFile pattern replacement", file=sys.stderr)
        sys.exit(1)

def read():
    with open(sys.argv[1]) as f:
        text = f.read() # ein einziger, grosser string, die ganze Datei
    return text

def replacer(old_text):
    neu_text = old_text.replace(sys.argv[3], sys.argv[4])
    return neu_text

def write(neu_text):
    with open(sys.argv[2], "w") as f:
        f.write(neu_text)
try:
    # E-ingabe
    text = read()
    # V-erarbeitung
    neu_text = replacer(text)
    # A-usgabe
    write(neu_text)

    sys.exit(0)
except Exception as e:
    print("FEHLER: ", e, file=sys.stderr)
    sys.exit(2)