FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv"

with open(FNAME) as fd:
    zeilen = fd.read().splitlines()

header = zeilen[0].replace(" ", "").split(",")
daten = []

for zeile in zeilen[1:]:
    if zeile.strip() != "":
        zeile = zeile.replace(" ", "").replace("$", "").split(",")
        einzelwert = {}
        for i, key in enumerate(header):
            if "." in zeile[i]:
                zeile[i] = float(zeile[i])
            elif zeile[i].isdigit():
                zeile[i] = int(zeile[i])
            einzelwert[key] = zeile[i]
        daten.append(einzelwert)

print(daten)
