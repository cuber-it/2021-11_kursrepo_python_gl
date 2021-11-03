#! /usr/bin/env python3
import pprint

d = {
    "Herausgeber": "Xema",
    "Nummer": "1234-5678-9012-3456",
    "Deckung": 2e+6,
    "Waehrung": "EURO",
    "Inhaber":
    {
        "Name": "Mustermann",
        "Vorname": "Max",
        "maennlich": True,
        "Hobbys": ["Reiter", "Golfen", "Lesen"],
        "Alter": 42,
        "Kinder": [],
        "Partner": None
    }
}
# print(d.get("Besitzer", None))
# print(d["Herausgeber"])
# d["Inhaber"]["Hobbys"].append("Schlafen")
# print(d)

# d = {
#     "Header": ["Datum", "Last", "High","Volume"]
#         }

#apple_stock = {
    #{"Datum: 21.1.21",
    #"Last: 355,0",
    #"High: 400,0",
    #"Volume: 400000"
    #}
#}

for test in d.keys():
    if isinstance(d[test], dict):
        print(d[test]["Alter"])
    # print(test)
    # if isinstance(d[test], dict):
    #     pprint.pprint(d[test][Alter])