#!/usr/bin/env python3
#Beispiel für Funktionen
import sys
import os
import random
import datetime

#if len(sys.argv) != 4:
#    print(f"usage{sys.argv[0]} py-InFile py-Outfile patern replacement", firl=sys.stderr)
#    sys.exit(1)
# rest aus Beispiel


def mach_was():
    result = random.sample(range(1,50),6)
    return result
    
x = mach_was()
print(x)

def f1(p,o1=0, o2=None,o3="",*args, **kwargs):
    print(p)
    print(o1,o2,o3)
    print(args)
    print(kwargs)

f1(4711)
f1(4712,99,100,101,102,103,104,x=1,y=2,z=3)

def sum(*args):
    result =0
    for zahl in args:
        result += zahl
    return result
print(sum(1,2))
print(sum(1,2,3,4,5,6,7))

t = datetime.datetime.now()
print(t)



