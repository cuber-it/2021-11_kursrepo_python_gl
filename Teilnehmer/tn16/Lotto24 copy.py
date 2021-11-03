#!/usr/bin/env python3

numbers_input = input("Geben Sie sechs Zahlen ein (durch Komma getrennt): ")
numbers_string = numbers_input.split(",")
##numbers = [int(numbers_string[i]) for i in range(len(numbers_string))]
#print (numbers)
if len(numbers_string) != 6: #<--- numbers -> numbers_string
    print ("Länge passt nicht", numbers_string) #<--- numbers -> numbers_string
    exit

tip = []
for zahl in numbers_string: #<--- numbers -> numbers_string
    if not zahl.isdigit():
        print(" keine Zahl:", zahl)
        exit()
    zahl = int(zahl)
    if not ( 1 <= zahl <= 49):
        print ("nicht gültig: ", zahl)
        exit()
    tip.append(zahl)
if len(set(tip)) != len(tip):
    print("Doppelt")       
    exit()
