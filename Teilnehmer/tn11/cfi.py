#!/usr/bin/env python3
import sys
import os

inp1=input("Zahl1 = ")
inp2=input("Zahl2 = ")
op_code=input("Operation (add,sub,mul,div) = ")
if inp1.isdigit():
    z1=int(inp1)
    if inp2.isdigit():
        z2=int(inp2)
        if op_code=="add":
            print(z1+z2)
        elif op_code=="sub":
            print(z1-z2)
        elif op_code=="mul":
            print(z1*z2)
        elif op_code=="div":
            print(str(z1//z2)," Rest ",str(z1%z2))
        else:
            print("Die Eingabe ",op_code," ist keine gültige Operation")
    else:
        print("Die Eingabe ",inp2," ist keine ganze Zahl")    
else:
    print("Die Eingabe ",inp1," ist keine ganze Zahl")
