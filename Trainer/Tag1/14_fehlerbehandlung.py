#!/usr/bin/env python3

# Vorsorgefall
eingabe = input("Eine Zahl != 0: ")

if not eingabe.isdigit() or int(eingabe) == 0:
    print("Das war nix")
    exit()

print(1/int(eingabe))

# Versuch und Irrtum
eingabe = input("Eine Zahl != 0: ")

try:
    print(1/int(eingabe))
except:
    print("Das war nix")
    exit()
