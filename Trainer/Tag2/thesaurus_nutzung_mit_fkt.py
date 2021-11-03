#!/usr/bin/env python3
fname = "/home/coder/Workspace/kurse_python_gl/Materialien/openthesaurus.txt"

def slurp(fname):
    with open(fname) as fd:
        daten = fd.read().splitlines()[18:]
    return daten

def build_wordlist(daten):
    wortliste = []
    for zeile in daten:
        wortliste.append(zeile.split(";"))
    return wortliste

def find_synonyms(daten):    
    while True:
        eingabe = input("Ihr Wort: ")
        if eingabe == "###":
            break
        for worte in daten:
            if eingabe in worte:
                print("Alternativen sind: ", worte)

"""
#print(dir())
daten = slurp(fname)
wordl = build_wordlist(daten)

find_synonyms(wordl)

print("Ende!")
"""