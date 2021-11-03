#!/usr/bin/env python3
import sys

def read(filenames):
    dateiliste = []
    for datei in filenames:
        with open(datei) as f:
            text = f.read()
            dateiliste.append({ "NAME": datei,
                                "SIZE": len(text),
                                "TEXT": text})
    return dateiliste

def write(fname, data):
    with open(fname, "w") as f:
        for file in data:
            print("-"*120, file=f)
            print(file["NAME"], file["SIZE"], file=f)
            print("-"*120, file=f)
            print(file["TEXT"], file=f)
            print("="*120, file=f)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]}, outfile, inputfile1, ...", file=sys.stderr)
        sys.exit(1)
    
    try:
        daten = read(sys.argv[2:])
        write(sys.argv[1], daten)
        sys.exit(0)
    except Exception as e:
        print("Fehler: ", e)
        sys.exit(2)