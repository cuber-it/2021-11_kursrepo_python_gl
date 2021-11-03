import re

regex = r"^def .*\(.*\):"

eingabe = input("Den Dateinamen: ")
with open(eingabe) as fd:
    test_str = fd.read()

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum = matchNum, 
        start = match.start(), 
        end = match.end(), 
        match = match.group()))
