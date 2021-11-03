#!/usr/bin/env python3
import sys
import os

def leseDatei(fname):
    with open(fname) as fd:
        daten = fd.read()
    return daten

def alleDateien():
    all_files = os.listdir('/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn10/')
    return all_files


#var = leseDatei("/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn10/aufgabe_1.py")
#print("aufgabe_1.py", var)
var_all = alleDateien()
print("Dateien: ",var_all, "Anzahl: ", len(var_all))
