import os
import glob

#dir(os)
#dir(glob)

path = input("Verzeichnis: ")
pattern = input("Dateinamenmuster: ")


found = glob.glob(os.path.join(path, pattern))

datei_inhalte = []
for fname in found:
    #print(fname)   #das hier zeigt nur an welche drin sind
    #mit dem was hier kommt ist zum öffnen von allen files 
    with open(fname) as fd:
        zeilen = fd.read().splitlines()
    datei_inhalte.append((fname, zeilen))
    
print(datei_inhalte)
        