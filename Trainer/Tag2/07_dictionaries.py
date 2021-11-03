#!/usr/bin/env python3

d = {"Ort": "HH", "Naem":"Willi"}
# Variante 1
try:
    print(d["Name"])
except KeyError:
    print("Nix")

# Variante 2
print(d.get("Name", "Nix"))

# Variante 3
if "Name" in d:
  print(d["Name"])
else:
  print("Nix")

print(d.keys())
print(d.values())
print(d.items())
#-------------------------

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

print("-" * 80)
car = {

  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
car.update({"brand": "Ford Car Company"})

print(car)