#!/usr/bin/env python3

import sys
import os
import pandas as pd

def read(input_datei):
    daten=[]
    with open(input_datei) as fd:
        text=fd.read().splitlines()
    for line in text[1:]:
        daten.append(line.split(","))
    return daten
#    return pd.read_csv(input_datei) # wird als dataframe ausgegeben

def get_BMI_and_status(rohdaten):
    bmi_tabelle=[]
    for line in rohdaten:
        name=line[0]
        groesse=float(line[2])/100.0
        gewicht=float(line[3])
        bmi=gewicht/(groesse*groesse)
        if bmi < 18.5:
            status = "-"
        elif bmi < 24.9:
            status = "+"
        elif bmi < 29.9:
            status = "-"
        elif bmi < 34.9:
            status = "--"
        elif bmi < 39.9:
            status = "---"
        else:
            status = "----"
        bmi_tabelle.append([name,bmi,status])
    return bmi_tabelle

def write(bmi_werte,ofname):
    with open(ofname, "w") as of:
        print("Name","BMI","Bewertung",file=of)
        for lines in bmi_werte:
            print(lines[0],lines[1],lines[2],file=of)


FNAME = f"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn11/AlterGroesseGewicht.csv"
OFNAME = f"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn11/BMI_Tabelle.dat"
input_daten=read(FNAME)
bmi_tabelle=get_BMI_and_status(input_daten)
write(bmi_tabelle,OFNAME)