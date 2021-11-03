#!/usr/bin/env python3
"""
fname_a = ""
fname_b = ""

fd = open(fname_a, "r")
text = fd.read()
fd.close()

with open(fname_b, "w") as fd: # close wird automat bei Blockende aufgerufen
    fd.write(text)

def text_file_copy(fname_a, fname_b):
    with open(fname_a) as fd:
        text = fd.read()
    with open(fname_b, "w") as fd:
        fd.write(text)
"""
fname = r"/home/coder/aktueller-kurs/materialien/openthesaurus.txt"
with open(fname) as fd:
        zeilen = fd.readlines() # slurp = alles auf einmal in den speicher!!!

for lnr, zeile in enumerate(zeilen[:20]):
    print(f"{lnr+1:>2} {zeile.rstrip()}")


# nachbau von enumerate <=> generatoren, filter
def my_enumerate(liste):
    counter = 0
    for e in liste:
        yield (counter, e)
        counter += 1



