fname = r"/home/coder/Workspace/aktueller-kurs/Materialien/sample.log.txt"
#!/usr/bin/env python3
import datetime

# Eingabe
fd = open(fname, "r")
text = fd.readlines() # der Text wird in eine Liste von Zeilen umgewandelt
fd.close()

# Verarbeitung und Ausgabe
print("-" * 80)
print("TRACE wurde zu folgenden Uhrzeiten gefunden:")
zeiten = []
for zeile in text:
    if "TRACE" in zeile:
        print(f"{zeile[6:14]}")
        zeiten.append(zeile[6:14])
        zeit = zeile[6:14]
        h = int(zeit[:2])
        m = int(zeit[3:5])
        s = int(zeit[6:])
        zeiten.append(datetime.time(h, m, s))

# Ausgabe
print("-" * 80)
print("TRACE wurde zu folgenden Uhrzeiten gefunden:")
print(f"Anzahl {len(zeiten)}")
print(zeiten)