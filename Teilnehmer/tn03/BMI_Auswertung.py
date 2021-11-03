#!/usr/bin/env python3
import sys

def read(filename):
    with open(filename) as fd:
        text = fd.read()
        local_list = text.replace(" ", "").splitlines()
        local_list = local_list[1:]
    return local_list

fname = input("Name der BMI-Datei: ")
bmi_list = read(fname)
print(bmi_list)