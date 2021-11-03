#!/usr/bin/env python3
import sys
import os
import random

def mach_was():
    result=random.sample(range(1,50),6)
    return result

x = mach_was()
print(*x)

print("Kommandozeile: ", sys.argv)
