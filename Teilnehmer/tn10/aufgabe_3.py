#!/usr/bin/env python3


simple_list = []
simple_set = {}
print("Geben Sie sechs Zahlen zwischen 1 und 49 an: ")

grenze = 6
maximum = 49
var = 0

for eingabe in range(1, int(maximum)):
    eingabe=input("Werteingabe: ")
    simple_set = simple_set + eingabe
    if eingabe not in simple_set:  
        var = var+1
        simple_list.append(eingabe)
        if var < grenze:
            break

#simple_list = simple_set
print (simple_list)