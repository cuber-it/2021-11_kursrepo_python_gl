#!/usr/bin/env python3
l = [ 1, 2, 3, 1, 5, 3, 7, 2 ]
#Aufgabe: alle doeppelten rausschmeissen:
s = set(l)
print(s)

l = list(s)
print(l[-1])

print("-" * 80)

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

print(s1 | s2)
print(s2 | s1)
print(s1 - s2)
print(s2 - s1)
print(s1 & s2)
print(s2 & s1)