#!/usr/bin/env python3
import sys

def read(filenames):
    collection = []
    for name in filenames:
        with open(name) as fd:
            text = fd.read()
            element = { "NAME": name, "SIZE": len(text), "TEXT": text}
            collection.append(element)
    return collection

def write(fname, data):
    with open(fname, "w") as fd:
        for file in data:
            print("-"*120, file=fd)
            print(file["NAME"], file["SIZE"], file=fd)
            print("-"*120, file=fd)
            print(file["TEXT"], file=fd)
            print("="*120, file=fd)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} outfile inputfile ...", file=sys.stderr) 
        sys.exit(1)

    try:
        daten = read(sys.argv[2:])
        write(sys.argv[1], daten)
        sys.exit(0)
    except Exception as e:
        print("Fehler: ", e)
        sys.exit(2)