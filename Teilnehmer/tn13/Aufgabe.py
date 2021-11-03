#!/usr/bin/env python3
import csv
fname=r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn13/bmidata.csv"
fdname=r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn13/pro.csv"

protokol=[]
fw=open(fdname,'w')
writer = csv.writer(fw)
with open(fname,'r') as fd:
    for zeile in fd:
        zeile=zeile.replace(" ","")
        name = zeile.split(",")[0]
        gross=int(zeile.split(",")[2])
        gewicht=int(zeile.split(",")[3])
        
        bmi = round(gewicht/((gross/100)*(gross/100)),2)
        if bmi < 18.5:
            stat=" untergewicht"
        elif bmi >18.5 and bmi < 24.9:
            stat=" nomralgewicht"
        elif bmi >25 and bmi < 29.9:
            stat=" Übergewicht"
        elif bmi >30 and bmi < 34.9:
            stat=" Starkes Übergewicht"
        elif bmi >35 and bmi < 39.9:
            stat=" Adipositas grad II"
        elif bmi > 40:
            stat=" Adipositas grad III"
        
        P=[name, bmi, stat]
        print(P)
        writer.writerow(P)
fw.close()
