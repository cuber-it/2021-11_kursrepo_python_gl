#!/usr/bin/env python3

FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"
f = open(FNAME, "r")
#text = f.read() # reads text file as one string
#l= f.readlines()
l= f.read().split("\n")
#l= f.read().splitlines()
#print(l[:5])
f.close()

zeilen = l[18:] #ignoriert die kommentarzeilen mit #
while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() =="_exit_":
        break
    for zeile in zeilen:
        if eingabe in zeile:
            print("Alternativen", zeile)

'''
with open(FNAME, r) as f:
    text = f.read()
#this has the closing command included'''