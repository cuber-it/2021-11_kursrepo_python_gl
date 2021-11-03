#!/usr/bin/env python3
def funktion_1(a):
    assert isinstance(a, int), 'Argument of wrong type!' 

def funktion_2(a):
    if not isinstance(a, int):
        raise TypeError("Invalid Type")  

def funktion_3(a): # das ist eher das typische Vorgehen in py: Versuch und Irrtum.
    v = int(a)

#funktion_1(4711)
#funktion_2(4711)
funktion_3(4711)