# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"\,[0-9]+"

fName = r"/home/coder/Workspace/aktueller-kurs/Teilnehmer/tn15/input_daten"
with open(fName) as fid:
    inhalt = fid.read().splitlines()[1:]

alter = []
groesse = []
gewicht = []
bmi = []

n = 0
for zeile in inhalt:
    zeilensplit = zeile.split(",")
    alter.append(int(zeilensplit[1]))
    groesse.append(int(zeilensplit[2]))
    gewicht.append(int(zeilensplit[3]))

    bmi.append(gewicht[n] / (groesse[n] / 100)**2)
    n += 1

    
print(alter)
print(groesse)
print(gewicht)
print(bmi)

# bmi = groesse[0]**2

# print(bmi)
# print("Name,Alter,Grösse,Gewicht")
# for n in range(3):
#     print(alter[n], )


# test_str = ("Name,Alter,Grösse,Gewicht\n"
# 	"\"Willi\",55, 198, 105\n"
# 	"\"Heinz\",65, 150, 95\n"
# 	"\"Klaus\",25, 185, 76")


# matches = re.finditer(regex, inhalt, re.MULTILINE)

# age = []
# for matchNum, match in enumerate(matches, start=1):
    
#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
#     age.append(match.group()[1:])
#     # for groupNum in range(0, len(match.groups())):
#     #     groupNum = groupNum + 1
        
#     #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
# print(age)
