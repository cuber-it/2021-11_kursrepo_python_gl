#!/usr/bin/env python3
d = {}

d["Name"] = "Willi"
d["PLZ"] = None
d["Ort"] = None
d["Strasse"] = None

print(d)

d["PLZ"] = "01234"
d["Otr"] = "Watzingen"

print(d)

d["Ort"] = "Watzingen"
del d["Otr"]


d["otr"] = "Watzingen"
print("Popitem:", d.popitem())

print(d)

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)