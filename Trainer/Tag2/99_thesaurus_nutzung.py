#!/usr/bin/env python3
fname = "/home/coder/Workspace/kurse_python_gl/Materialien/openthesaurus.txt"

with open(fname) as fd:
    daten = fd.read().splitlines()[18:]

wortliste = []
for zeile in daten:
    wortliste.append(zeile.split(";"))

while True:
    eingabe = input("Ihr Wort: ")
    if eingabe == "###":
        break
    for worte in wortliste:
        if eingabe in worte:
            print("Alternativen sind: ", worte)
