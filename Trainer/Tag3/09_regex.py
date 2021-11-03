#!/usr/bin/env python3
"""
\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs
"""
import pprint
import re

pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
fname = r"/home/coder/aktueller-kurs/materialien/SampleLog.log"

with open(fname) as fd:
    zeile = fd.read().splitlines()

rex = re.compile(pattern, re.I)

ergebnis = []
for lnr, zeile in enumerate(zeile):
    if rex.search(zeile):
        ergebnis.append((lnr, zeile))

# pprint.pprint(ergebnis)    
for z in ergebnis:
    print(z)    