#!/usr/bin/env python3
import sys

def read(filenames):
    collection=[]
    for fname in filenames:
        with open(fname) as fd:
            text = fd.read()
            collection.append({ "Name": fname,
                                "Size": len(text),
                                "Text": text })
    return collection
        

def write(fname,data):
    with open(fname,"w") as fd:
        for file in data:
            print("-"*100, file=fd)
            print (file["Name"],file["Size"], file=fd)
            print("-"*100, file=fd)
            print(file["Text"], file=fd)
            print ("="*100, file=fd)
             

