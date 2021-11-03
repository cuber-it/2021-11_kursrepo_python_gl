#!/usr/bin/env python3
fname = "/home/coder/Workspace/kurse_python_gl/Materialien/Sample.log"

# Eingabe
with open(fname) as fd:
    daten = fd.read()

# Verarbeitung
report_daten = {}
for zeile in daten.splitlines():
    key = zeile[15:22].strip()
    if key in report_daten:
        report_daten[key] += 1
    else:
        report_daten[key] = 1

# Ausgabe
print("Report")
print("-" * 60)
for k, v in report_daten.items():
    print(f"{k}\t\t{v:>10}")
print("-" * 60)
