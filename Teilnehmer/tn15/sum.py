#! /usr/bin/env python3

def sum(*args):
    result = 0
    if args:
        if isinstance(args[0], list):
            args = args[0]
        for zahl in args:
            result += zahl
    return result

if __name__ == "__main__": # verhindert dass die Folgezeilen bei Laden als Modul ausgeführt werden
    e = sum()
    assert e==0, "Summierungsfehler"

    e = sum(0)
    assert e==0, "Summierungsfehler"

    e = sum(1,2)
    assert e==3, "Summierungsfehler"

    e = sum([1,2])
    assert e==3, "Summierungsfehler"

#print(sum(1,2))
#print(sum([1,2,3,4,5,6,7,8,9,10]))