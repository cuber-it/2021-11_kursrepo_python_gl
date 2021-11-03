'''
with open(r"/home/coder/Workspace/aktueller-kurs/Materialien/HistoricalQuotes.csv") as f:
    zeilen = f.read().splitlines()

header = zeilen[0].replace(" ", "").split(",")
daten = []
for zeile in zeilen[1:]:
    worte = zeile.replace(" ", "").split(",")
    for i in range(0, len(worte)):
        if worte[i].startwith("$"):
            worte[i] = float(worte[i].replace("$", ""))
    daten.append(worte)

    print(daten)

import pandas
df = pandas.DataFrame(daten)
print(df)
'''


l1=[True, False, True, True]
l2=[1,2,3,4]
for i, status in enumerate(l1):
    if status == True:
        print(l2[i])