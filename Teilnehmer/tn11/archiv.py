#!/usr/bin/env python3
import sys

def read(fnames):
    myDict={}
    for fname in fnames:
        with open(fname) as fn:
            text=fn.read()
        Anzahl_Zeichen=len(text)
        myDict[fname]=[Anzahl_Zeichen,text]
    return myDict

def write(fname_out,daten_in):
    with open(fname_out,"w") as fd:
        for fname_in, values in daten_in.items():
            print("-"*100, file=fd)
            print(fname_in, values[0], file=fd)
            print("-"*100, file=fd)
            print(fname_in, values[1], file=fd)
            print("-"*100, file=fd)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} outfile inputfile ...", file=sys.stderr)
        sys.exit(1)
    try:
        daten=read(sys.argv[2:])
        write(sys.argv[1],daten)
        sys.exit(0)
    except Exception as e:
        print("Fehler: ", e)
        sys.exit(2)