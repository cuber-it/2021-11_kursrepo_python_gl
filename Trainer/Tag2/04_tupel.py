#!/usr/bin/env python3
l = [1, 2, 3]
t = (1, 2, 3)

print(t == l)

l[0] = 4711
# t[0] = 4711 # gibt Exception

print(l[0])
print(t[0])

l.append(4711)
# t.append(4711)

l = list(t) # legt kopie des tupels als liste an
l[0] = 4711
print(t[0])
print(l[0])

a = [4711, 2, 3]
b = [1, None]
c = [None, 2]

t = (a,b,c)
print(t)

t[0][0] = 5
t[1][0] = None
t[2][0] = 4711

print(t)