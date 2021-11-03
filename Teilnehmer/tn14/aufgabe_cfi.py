#!/usr/bin/env/ python3
import sys
import os
eingabe1=input("Eingabe1 (Zahl): ")
print(type(eingabe1))
print(eingabe1)
if eingabe1.isdigit():
    print("Eingabe 1 ist eine Ganzzahl")
    eingabe1=int(eingabe1)
else:
    print("Eingabe 1 ist keine Zahl")
    exit()
eingabe2=input("Eingabe2 (Zahl): ")
print(type(eingabe2))
print(eingabe2)
if eingabe2.isdigit():
    print("Eingabe 2 ist eine Ganzzahl")
    eingabe2=int(eingabe2)
else:
    print("Eingabe 2 ist keine Zahl")
    exit()
eingabe3=input("Operation: add ,sub, mul, div ?: ")
print(type(eingabe3))
print(eingabe3)
if eingabe3.isdigit():
    print("Eingabe 3 ist kein String !!!")


if eingabe3 =="add":
    ergebnis = eingabe1 + eingabe2
    print("Summe =",ergebnis)
    exit()
if eingabe3 =="sub":
    ergebnis = eingabe1 - eingabe2
    print("Differenz =",ergebnis)
    exit()
if eingabe3 =="mul":
    ergebnis = eingabe1 * eingabe2
    print("Produkt= ",ergebnis)
    exit()
if eingabe3 =="div":
    ergebnis = eingabe1 // eingabe2
    rest = eingabe1 % eingabe2
    print("Quotient= ",ergebnis)
    print("Rest= ",rest)
