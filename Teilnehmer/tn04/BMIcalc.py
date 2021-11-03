FNAME = r"/home/coder/Workspace/aktueller-kurs/Materialien/openthesaurus.txt"
f = open(FNAME, "r")
#text = f.read() # reads text file as one string
#l= f.readlines()
l= f.read().split("\n")
#l= f.read().splitlines()
#print(l[:5])
f.close()