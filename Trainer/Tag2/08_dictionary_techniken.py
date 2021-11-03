#!/usr/bin/env python3
def daten():
    return ["Watz", "willi", "12345", "Watzingen", "Watzplatz 1"]


#----
def make_dict(h, daten):
    v = daten() 
    if len(h) == len(v):
        d = dict(zip(h, v))
    else:
        raise ValueError("Daten passen nicht")
    return d


# ----
h = ["Name", "Vorname", "PLZ", "Ort", "Strasse", "Hausnr"]
try:
    d = make_dict(h, daten)
    print(d)
    exit(0)
except ValueError as e:
    print("allgemeiner Fehler:", e)
    exit(1)