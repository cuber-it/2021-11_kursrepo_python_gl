import re

regex = r"(([0-9]{1,3}\.){3}[0-9]{1,3})"

with open("/home/coder/Workspace/kurse_python_gl/Materialien/Sample.log") as fd:
    test_str = fd.read()

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum = matchNum, 
        start = match.start(), 
        end = match.end(), 
        match = match.group()))
    
    