#!/usr/bin/env python3
l = [ 1, 2.34, "Willi", None, True]
print("Typ", type(l))

print("-" * 80)

for e in l:
    print("Type: ", type(e))
    print("Elementwert: ", e)

print("-" * 80)

# geht auch, eher untypisch in python
i = 0
while i < len(l):
    print("Type: ", type(l[i]))
    print("Elementwert: ", l[i])
    i = i + 1 # alternativ: i += 1 
