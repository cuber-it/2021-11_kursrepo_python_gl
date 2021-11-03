#!/usr/bin/env python3

zahl_1 = input("Zahl 1 (INT): ")
zahl_2 = input("Zahl 2 (INT): ")
op_code = input("Operation (add, sub, mul, div): ")

if zahl_1.isdigit():
    zahl_1 = int(zahl_1)
    if zahl_2.isdigit():
        zahl_2 = int(zahl_2)
        if op_code == "add":
            ergebnis = zahl_1 + zahl_2
            print("Ergebnis: ", ergebnis)
        elif op_code == "sub":
            ergebnis = zahl_1 - zahl_2
            print("Ergebnis: ", ergebnis)
        elif op_code == "mul":
            ergebnis = zahl_1 * zahl_2
            print("Ergebnis: ", ergebnis)
        elif op_code == "div":
            ergebnis = zahl_1 // zahl_2
            rest = zahl_1 % zahl_2
            print("Ergebnis: ", ergebnis)
            print("Rest: ", rest)
        else:
            print("Falscher opcode: ", op_code)
    else:
        print("Zahl 2 kein int: ", zahl_2)
else:
    print("Zahl 1 kein int: ", zahl_1)        
    
