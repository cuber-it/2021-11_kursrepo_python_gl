def sum(*args):
    result = 0
    if args:
        if isinstance(args[0], list):
            args = args[0]
        for zahl in args:
            result += zahl
    return result

if __name__ == "__main__"    : # verhindert dass die Folgezeilen bei Laden als modul ausgeführt werden
    e = sum()
    assert e==0, "Summierungsfehler"

    e = sum(0)
    assert e==0, "Summierungsfehler"

    e = sum(1,2)
    assert e==3, "Summierungsfehler"

    e = sum([1,2])
    assert e==3, "Summierungsfehler"

    # von hier aus kann man dann unittest sich mal ansehen!!
    # ..
