#!/usr/bin/env python3

l1 = []
l2 = [1, 2, 3, 4]
l3 = [1, 2.5, "Hey", None, True]
l4 = list(range(0, 10)) # range(von, bis) geht immer [von..bis-1]
l5 = list()
l6 = list("Hello, world")
l7 = "Uhrzeit:Datum:Ereignis:Meldung".split(":")
l8 = [l1, l2, l3, l4, l5, l6, l7] # Liste von Listen

print(l1)
print(l2)

print("-" * 80)

for n in l8:
    print(type(n))
    print(n)

print(l8)

# Wo range gerne eingesetzt wird
# for i in range(0, 10, 2):
#    print(i)
print("-" * 80)

"""
l9 = l8 # Beide zeigen auf den gleichen Speicher
l9.append(["Hello", "world"])
print(l9)
print(l8)

print("-" * 80)

l9 = l8[:] # Eine FLACHE!!!! Kopie von l8 für l9 angelegt
l9.append(["Hello", "world"])
print(l9)
print(l8)

print("-" * 80)

l9[0].append("ALOHA") # da es ein flache Kopie ist, ist l8 auch wieder betroffen!
print(l9)
print(l8)
"""