#!/usr/bin/env python3

import sys
import re

class LogReader:
    _rex_crap = re.compile(r"(^ *$)|( \d\d )|(^Kopieren)")
    _rex_regular = re.compile(r"^\d\d/\d\d")

    def __init__(self, input_name, output_name):
        self._input_name = input_name
        self._output_name = output_name
        self._raw_text = []
        self._cooked_text = []

    def read_file(self):
        with open(self._input_name) as fd: # standard: r
            self._raw_text = fd.read().splitlines()

    def write_file(self):
        with open(self._output_name, "w") as fd:
            fd.write("\n".join(self._cooked_text))

    def _is_crap(self, zeile):
        return self._rex_crap.search(zeile)

    def _is_regular(self, zeile):
        return self._rex_regular.search(zeile)

    def cleanup_log(self):
        self._cooked_text = []
        for zeile in self._raw_text:
            if self._is_crap(zeile): 
                continue
            if self._is_regular(zeile): # ist das eine echte neue Zeile oder ein Umbruch
                self._cooked_text.append(zeile) # die Zeile ist neu
            else:
                self._cooked_text[-1] += zeile # Umbruch an der vorhergehenden anhängen
        return self._cooked_text # Für den Fall dass der Benutzer intern mit den Daten weiterarbeiten will

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: log_reader input_logfile_name output_logfile_name")
        exit(1)

    infname = sys.argv[1]
    outfname = sys.argv[2]

    lr = LogReader(infname, outfname)
    lr.read_file()
    lr.cleanup_log()
    lr.write_file()

    exit(0)