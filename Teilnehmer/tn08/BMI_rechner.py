#!/usr/bin/env python3
FILENAME = r"bmi-tabelle.csv"
SPEICHERDATEI = r"bim-erg.txt"

def bmirechener(groesse, gewicht):
    groesse = groesse / 100.0
    bmi = float(gewicht/gewicht)
    bewertung = ""
    if (18.0 <= bmi <= 23.5):
        bewertung = "+"
    elif (16.6 <= bmi <= 26.3):
        bewertung = "-"
    elif (15.2 <= bmi <= 27.7):
        bewertung = "--"
    else:
        bewertung = "---"
    return bmi, bewertung



with open(FILENAME, "r") as f:
    zeilen = f.readlines()
daten = []
for zeile in zeilen[1:]:
    try:
        daten.append({"Name": zeile.split(",")[0], "Alter": zeile.split(",")[1], "Groesse": zeile.split(",")[2], "Gewicht": zeile.split(",")[3] })
    except:
        print("zeile konnte nicht ausgelesen werden")
        exit()

with open(SPEICHERDATEI, "w") as fd:
    print(daten[0] + ", BMI, BMI bewertung")
    
