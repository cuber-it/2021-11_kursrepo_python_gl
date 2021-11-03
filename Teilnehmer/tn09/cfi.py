#!/usr/bin/env python3
import sys
import os

input_1_zahl = input("Eingabe Zahl 1: ")
if input_1_zahl.isdigit():
    input_1_zahl = int(input_1_zahl)
else:
    print("Keine Zahl:")
    exit()
input_2_zahl = input("Eingabe Zahl 2: ")
if input_2_zahl.isdigit():
    input_2_zahl = int(input_2_zahl)
else:
    print("Keine Zahl:")
    exit()
    
input_3_opcode = input("Eingabe Operation: ")
if input_3_opcode == 'add' or input_3_opcode == 'mul' or input_3_opcode == 'div' or input_3_opcode == 'sub' or input_3_opcode == 'div_mod':
    #print("lets go!")
    if input_3_opcode == 'add':
        ergebnis = input_1_zahl + input_2_zahl
    elif input_3_opcode == 'mul':
        ergebnis = input_1_zahl * input_2_zahl    
    elif input_3_opcode == 'div':
        ergebnis = input_1_zahl // input_2_zahl
    elif input_3_opcode == 'div_mod':
        ergebnis = str(input_1_zahl // input_2_zahl) + ' Rest: ' + str(input_1_zahl % input_2_zahl)
        print(ergebnis)
    elif input_3_opcode == 'sub':
        ergebnis = input_1_zahl - input_2_zahl
else:
    print("Kein aktzeptierter op-code!") 


print("Ergebnis: ", ergebnis)     