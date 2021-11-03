#!/usr/bin/env python3
import json

file = "/home/coder/aktueller-kurs/materialien/config.json"

daten = json.load(open(file))
print(type(daten))

for servlet in daten["web-app"]["servlet"]:
    print(servlet["servlet-name"])

