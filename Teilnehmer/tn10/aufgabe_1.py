#!/usr/bin/env python3
import sys
import os

ein1 = input("Eingabe der esten Zahl: ")
ein2 = input("Eingabe der zweiten Zahl: ")
op_code = input("add, sub, mul, div: ")

if ein1.isdigit() and ein2.isdigit():
    add = int(ein1) + int(ein2)
    sub = int(ein1) - int(ein2) 
    mul = int(ein1) * int(ein2)
    div = int(ein1) // int(ein2)
    mod = int(ein1) % int(ein2)
    if op_code == "add":
        print("Summe von",ein1, " und ",ein2, " ist: ", add)
    elif op_code == "sub":
        print("Differenz von",ein1, " und ",ein2, " ist: ", sub)
    elif op_code == "mul":
        print("Produkt von",ein1, " und ",ein2, " ist: ", mul)
    elif op_code == "div":
        print("Quotient von",ein1, " und ",ein2, " ist: ", div, " mit Rest: ", mod)
    else:
        print("Bitte nur add, sub, mul oder div eingeben!!")
else:
    print("Sie haben keine zwei zahlen eingegeben")