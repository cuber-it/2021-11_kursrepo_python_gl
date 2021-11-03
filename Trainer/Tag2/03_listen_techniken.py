#!/usr/bin/env python3
s = "Willi:Watz:Watzplatz:17:12345:Watzingen"
l = s.split(":") 
print(l)

n = "|".join(l) # String aus Liste mit | als Trenner. Idee wäre gewesen: l.join("|") aber in py sieht es halt anders aus
print(n)

# Gezielt variablen aus listen heraus füllen
# _ ist die default/dummy Variable
name = l[0]; ort = l[-1] # ist korrekt und gut
print(name, "aus",  ort)
name, _, _, _, _, ort = l # Liefert das gleiche wie Zeil 11, ist aber ein wenig nerdiger :-D _ ist die default Variable
print(name, "aus",  ort)

name, vorname, *adresse = l # Abtrenntechnik um Variablen zu füllen
# Entspricht: name = l[0]; vorname = l[1]; adresse = l[2:] liefert das gleiche Ergebnis, nur nicht so elegant
# oder gleich: name, vorname, adresse = s.split(":") 
print(name)
print(vorname)
print(adresse)

print("-" * 80)
a = 1
b = 100
# Aufgabe: tausche a mit b
b, a = a, b # intern wird temporär ein Tupel angelegt, deswegen klappt das
print("a:", a)
print("b:", b)

"""
print("-" * 80)
for n in ["Watzingen", "12345", "Am Platz", "10"]:
    if n in adresse:
        print(n, "identisch")
    else:
        print(n, "nicht gefunden")
"""
    