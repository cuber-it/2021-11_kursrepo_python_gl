#!/usr/bin/env python3
filepath = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"
#f = open(filepath,'r')
#text = f.read()
#f.close()

# moderne meist üblichere Schreibweise mit auto-close
with open(filepath,"r") as f:
    text=f.read()
#print(text[:100])
#print("Lange:", len(text))
#zeilen = text.split("\n")
zeilen = text.splitlines()
#print(zeilen[:5])
#print("Zeilenzahl:",len(zeilen))


while True:
    eingabe = input("Suchwort: ")
    if eingabe.lower() == "_exit_":
        break
    for zeile in zeilen[18:]:
        if eingabe in zeile:
            print("Alternativen: ",zeile)