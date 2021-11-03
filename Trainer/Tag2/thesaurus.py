#!/usr/bin/env python3
import thesaurus_nutzung_mit_fkt as T

fname = "/home/coder/Workspace/kurse_python_gl/Materialien/openthesaurus.txt"

#print(dir())
daten = T.slurp(fname)
wordl = T.build_wordlist(daten)

T.find_synonyms(wordl)

print("Ende!")