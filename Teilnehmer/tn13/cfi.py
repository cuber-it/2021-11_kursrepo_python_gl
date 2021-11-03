#!/usr/bin/env python3
import sys
import os
Z1 = input("Zahl 1 eingeben: ")
Z2 = input("Zahl 2 eingeben: ")
op_code = input("OP-code eingeben:") 
if Z1.isdigit() and Z2.isdigit() and op_code.lower() in ["add","sub","mul","div"]:
    if op_code.lower() == "add":
        Erg = int(Z1) + int(Z2)
        print(Z1, " add ", Z2, " ist ", Erg)
    elif op_code.lower() == "sub":
        Erg = int(Z1) - int(Z2)
        print(Z1, " sub ", Z2, " ist ", Erg)
    elif op_code.lower() == "mul":
        Erg = int(Z1) * int(Z2)
        print(Z1, " mal ", Z2, " ist ", Erg)
    elif op_code.lower() == "div":
        Erg1 = int(Z1) // int(Z2)
        Erg2 = int(Z1) % int(Z2)
        print(Z1, " div ", Z2, " : ", "Ganzzahl ist ", Erg1, "und Rest ist ", Erg2)
else:
    print("Eingabe ist Unsinn!!!")

