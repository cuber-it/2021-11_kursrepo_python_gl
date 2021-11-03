#!/usr/bin/env python3
import sys
import os
import random

def mach_was():
    result=random.sample(range(1,50),6) # 5 aus 49
    result2=random.sample(range(1,50),1) # Zusatzzahl
    return result,result2

x = mach_was()
print("TippZahlen: ",*x[0])
print("Zusatzzahl: ",*x[1])
