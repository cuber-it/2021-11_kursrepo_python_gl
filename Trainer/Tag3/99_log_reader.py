#!/usr/bin/env python3

import sys
import re

_rex_crap = re.compile(r"(^ *$)|( \d\d )|(^Kopieren)")
_rex_regular = re.compile(r"^\d\d/\d\d")

def read_file(fname):
    with open(fname) as fd: # standard: r
        zeilen = fd.read().splitlines()
    return zeilen

def write_file(fname, zeilen):
    with open(fname, "w") as fd:
        fd.write("\n".join(zeilen))

def _is_crap(zeile):
    return _rex_crap.search(zeile)

def _is_regular(zeile):
    return _rex_regular.search(zeile)

def cleanup_log(zeilen):
    ergebnis = []
    for zeile in zeilen:
        if _is_crap(zeile): 
            continue
        if _is_regular(zeile): # ist das eine echte neue Zeile oder ein Umbruch
            ergebnis.append(zeile) # die Zeile ist neu
        else:
            ergebnis[-1] += zeile # Umbruch an der vorhergehenden anhängen
    return ergebnis

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: log_reader input_logfile_name output_logfile_name")
        exit(1)

    infname = sys.argv[1]
    outfname = sys.argv[2]

    raw_data = read_file(infname)
    cooked_data = cleanup_log(raw_data)
    write_file(outfname, cooked_data)

    exit(0)