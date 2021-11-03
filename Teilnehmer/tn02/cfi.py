#!/usr/bin/env python3

eingabe = input("Zahl 1:")
if eingabe.isdigit():
    print("Inhalt ist eine Zahl")
    zahl1 = int(eingabe)


eingabe = input("Zahl 2:")
if eingabe.isdigit():
    print("Inhalt ist eine Zahl")
    zahl2 = int(eingabe)


eingabe = input("Operation code add,mul,div,sub:")
op = (eingabe)
print(eingabe)
if op == "add":
    ergebnis =( zahl1 +zahl2)
elif op == "sub":
    ergebnis = (zahl1-zahl2)

print( "Ergebnis = ",ergebnis)
    
