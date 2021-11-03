#!/usr/bin/env python3
with open("/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn16/BMI.csv","r") as tf:
  lines = tf.read().splitlines()
for line in lines:
    print(line)


bmi = float(gewicht) / (float(groesse) ** 2)

print("Der BMI ist: ", bmi)

if bmi < 18.5:
    print("Untergewicht")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normalgewicht")
elif bmi >= 24.9 and bmi < 29.9:
    print("Übergewicht")
else:
    print("Keine Schoki heute abend!!!")    
