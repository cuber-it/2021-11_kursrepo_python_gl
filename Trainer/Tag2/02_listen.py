#!/usr/bin/env python3
groesse = int(input("Wie gross soll es sein? "))
l1 = [0] * groesse # Erzeugt Liste mit 10 x 0
print(l1)

l2 = [1,2,3,4,5] # <=> l2 = list(range(1, 6))
print(l2)

l3 = l1 + l2 + [None, 7, 9, 8] # Neue Liste mit Kopien der Inhalte der Einzellisten angelegt, es werden flache Kopien angelegt
print(l3)

print("-" * 80)
print(l3[::2]) # Jedes zweite Element
print(l3[:len(l1)]) # Die ersten 10 Elemente ausgeben = Länge der Liste 1
print(l3[len(l1):]) # Ausser den elementen von Liste 1 wird alles ausgegeben

print("-" * 80)
l3.reverse()
print(l3)

#l3.sort() # - hat hier wegen None nicht geklappt, None muss weg!

print(l3.index(None))
#l3.pop(l3.index(None)) - oder s.u:
l3.remove(None)
print(l3)

l3.sort()
print(l3)

l3.sort(reverse=True)
print(l3)
print("-" * 80)

print(sorted(l3)) # liefert sortierte Liste zurück, ohne das Original zu verändern
print(l3)
"""
print("-" * 80)
l3[l3.index(1)] = 4711
print(l3)
print("-" * 80)

# Tipp: wir packen den Ersetzer in eine Funkion:
def list_replace(list_name, old_value, new_value):
  list_name[list_name.index(old_value)] = new_value 
  return list_name

list_replace(l3, 4711, 1)
print(l3)
"""


 



