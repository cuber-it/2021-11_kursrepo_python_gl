#!/usr/bin/env python3
import string

s = "Hello, world!"
print(list(s)) # Umwandeln Sting in Liste, Buchstabe für Buchstabe ["H", "e", "l", ... "d"]
print(len(s)) # Länge der Strings

print(s[0]) # 1. Buchstabe

print(s[11]) # 12. Buchstabe
print(s[len(s)-1]) # der letzte Buchstabe errechnet
print(s[-1]) # oder viel einfache der letzte Buchstabe

print(s[:5]) # die Buchstaben von 0 - 4
print(s[7:]) # die Buchstaben von Stelle 8 bis Ende (inkl!)

print(s[2:5]) # die buchstaben von Stelle 3 bis 4

print(s[:]) # 1:1 Kopie von 0 bis Ende
print(s[1::2]) # jeder 2. Buchstabe

s = """2021/03/09 10:35:10.1500\tOK Alles ist in Ordnung
2021/03/09 10:35:10.1500\tOK Alles ist in Ordnung
2021/03/09 10:35:10.1500\tOK Alles ist in Ordnung"""
print(s.split("\n")) # Zerlegung in einzelne Sätze
print(s.splitlines())

for zeile in s.splitlines(): # Zeilenweise Bearbeitung eines langen Textes
    print("Zeile: ", zeile[zeile.find("OK"):]) # Ab dem ersten AUftreten des OK bis Zeilenende ....

# Eine ASCII-Tabelle erzeugen
zeile = ""
for n in range(32,128): #Wertebereich 32-127"
    zeile += f"{n} : {chr(n)}\t" # unicode-Darstellung wird an Zeile angehängt - Gegenfunktion zu chr() ist ord()
    if n % 8 == 0: # Alle 8 zeichen ist Modulo 0 , d.h. ich will dass ein Umbruch erzeugt wird
        print(zeile) # Zeile ausgeben
        zeile = "" # Neue Zeile beginnen


# Meine Auskommentierung mittel langem String:
"""
print(string.ascii_lowercase) # Konstante der Klasse string, die alle gültigen Kleinbuchstaben enthält
print(s.lower()) # Methode der Klasse string, gebunden an Objekt s, um den Inhlat klein zurück zu geben

if s.isdecimal():
    print("ist eine Ganzzahl")
elif s.isalpha():
    print("ist nur Alphanumerisch")
elif s.isprintable():
    print("immerhin druckbar")
else:
    print("dann eben sonst was!")
"""