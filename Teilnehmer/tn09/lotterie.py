#!/usr/bin/env python3
import sys
import os

eingabe = "1,2,3,4,5,6" # 'for testing'


eingabe = "dummy"
while True:   #  oder while True und dann nach eingabe : If IP == exit: break
    eingabe = input("Please enter 6 numbers as string with , : ").lower()
    if eingabe == "exit":
        break
    if not "," in eingabe: 
        print("Zahlen nicht durch Kommas getrennt!")
    else:
        numbers = eingabe.split(",")
        if not len(numbers) == 6:
            print("Eingabe enthält keine 6 Zahlen")
        else:
            for ii in range(0,len(numbers)):
                if not numbers[ii].isdigit():
                    print("mindesten einer der 6 Zahlen ist kein Integer")
                    exit() 
            not_valid = []
            for number_i in numbers:
                if not (0< int(number_i) <=49):
                    not_valid.append(int(number_i))
            if len(not_valid) > 0: 
                print("folgende Zahl(en) ist/sind nicht im Bereich 1-49 !",  not_valid)
            else:
                doppelte_werte = set(numbers)
                if len(doppelte_werte) != len(numbers):
                    print("Es gibt doppelte Werte in der Eingabe")
                else:
                    print("Tipp ist: ", *numbers, " Thank you for playing")
    