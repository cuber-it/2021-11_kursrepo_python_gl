#!/usr/bin/env python3
import datetime

fname = r"/home/coder/Workspace/aktueller-kurs/Materialien/sample.log.txt"

# E_ingabe
fd = open(fname, "r")
text = fd.readlines() # der text wird in eine liste von zeilen umgewandelt
fd.close()

# V_erarbeitung
zeiten = []
for zeile in text:
    if "TRACE" in zeile:
        zeit = zeile[6:14]
        h = int(zeit[:2])
        m = int(zeit[3:5])
        s = int(zeit[6:])
        zeiten.append(datetime.time(h, m, s))


# A_usgabe
print("TRACE wurde gefunden zu folgenden Uhrzeiten:")
print("-" * 80)
print(f"Anzahl {len(zeiten)}")
print(zeiten)
