#!/usr/bin/env python3
import sys

def read(dateien):
    ausgabe = []
    for datei in dateien:
        str(datei)
        with open(datei, "r") as f:
            text = f.read()
        dateiname = datei.split("\\")[-1]
        zeichenanzahl = len(text)
        textinzeilen = text.split("\n")
        ergebise = {"Dateiname":dateiname, "Anzahl der Zeilen": len(textinzeilen), "Anzahl der Zeichen":zeichenanzahl, "Inhalt": text}
        ausgabe.append(ergebise)
    return ausgabe

def write(dateien, outdatei):
    with open(outdatei, "w") as fd:
        for datei in dateien:
            print("-" * 80, file=fd)
            print(datei("Dateiname") +"\tAnzahl der Zeilen: " + datei("Anzahl der Zeilen") + "\tAnzahl der Zeichen: " + datei("Anzahl der Zeichen"), file=fd)
            print("-" * 80, file=fd)
            print(datei("Inhalt"), file=fd)
            print("=" * 80, file=fd)




if len(sys.argv) < 3:
    dateien = read(sys.argv[2:])
    write(dateien, sys.argv[1])
