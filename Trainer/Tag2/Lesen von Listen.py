#!/usr/bin/env python3
FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"
# Klassische Schreibweise für Dateiöffnen
f = open(FNMAE, "r")
text = f.read() # Ganze Datei als ein String komlett eingelesen
f.close()
print(text[:100])
print("Länge:" , len(text))
