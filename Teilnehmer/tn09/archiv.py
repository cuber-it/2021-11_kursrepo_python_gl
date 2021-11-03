#!/usr/bin/env python3
import sys
import os

def read(files):
    data = []
    for name in files:
        with open(name) as fd:
            text = fd.read()
            element = {"NAME": name, "SIZE":len(text), "TEXT": text}
            data.append(element)
    return data

def write(fname, data):
    with open(fname,"w") as fd:
        for file in data:
            print("-"*120, file=fd)
            print(file["NAME"],file["SIZE"], file=fd)
            print("-"*120, file=fd)
            print(file["TEXT"], file=fd)
            print("-"*120, file=fd)




if __name__ == "__main__":
    print("len(sys.argv)", len(sys.argv))
    if len(sys.argv)< 3: print("sys.argv < 3")
    