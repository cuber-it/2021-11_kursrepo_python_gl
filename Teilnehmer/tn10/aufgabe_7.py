#!/usr/bin/env python3
import sys
import os

# Aufgabe BMI-Rechner

def leseDatei(fname):
    with open(fname) as fd:
        daten = fd.read()
    return daten

#def calculateBMI()


def processdata(name, bmivalue):
    if float(bmivalue) < 18.5:
        print(name, "hat mit. ", bmivalue, " Untergewicht")
    elif float(bmivalue) >= 18.5 and float(bimvalue) <= 24.9:
        print(name, "hat mit. ", bmivalue, " Normalgewicht")
    elif float(bmivalue) > 24.9 and float(bimvalue) <= 29.9:
        print(name, "hat mit. ", bmivalue, " leichtes Übergewicht")
    elif float(bmivalue) >= 30 and float(bimvalue) <= 34.9:
        print(name, "hat mit. ", bmivalue, " Übergewicht von Stufe 1")
    elif float(bmivalue) >= 35 and float(bimvalue) <= 39.9:
        print(name, "hat mit. ", bmivalue, " Übergewicht von Stufe 2")
    else:
        print(name, "hat mit. ", bmivalue, " Übergewicht von Stufe 3")


var = leseDatei("/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn10/bmidata.csv")
print("BMI-Daten", var)

