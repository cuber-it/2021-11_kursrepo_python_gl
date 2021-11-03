#!/usr/bin/env python3
import xmltodict
import json

fname = r"/home/coder/Workspace/kurse_python_gl/Materialien/books.xml"

with open("books.json", "w") as fd:
    fd.write(json.dumps(xmltodict.parse(open(fname).read()), indent=4))