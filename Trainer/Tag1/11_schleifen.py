#!/usr/bin/env python3
# V1
while True:
    eingabe = input("Ihre Eingabe: ")
    if eingabe.lower() == "exit":
        break
    print("Eingabe war: ", eingabe)

#V2
eingabe = ""
while eingabe.lower() != "exit":
    eingabe = input("Ihre Eingabe: ")
    if eingabe.lower() != "exit":
        print("Eingabe war: ", eingabe)
    
print("Ende")