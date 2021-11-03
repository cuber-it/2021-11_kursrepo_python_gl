#!/usr/bin/env python3
import re
print(re.search(r"M", "String mit M und M und M"))
print(re.findall(r"M", "String mit M und M und M"))

rex = re.compile(r"M")
print(rex.findall("String mit M und M und M"))

for m in rex.finditer("String mit M und M und M"):
    print(m)
