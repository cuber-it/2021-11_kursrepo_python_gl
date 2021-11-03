import random

def mach_was():
    result = random.sample(range(1,50),6)
    return result
# ohne return, kann man schlicht das was in der Funktion erzeugt wird nicht verwenden!!!
# trotzdem gibt es Funktionen ohne return, die nennt man dann Prozeduren. Meine Frage war dann "ist die dann nicht tot? 
# --> antwort: das benutzt man wenn man an dem "Effekt" interessiert ist, z.B. dass das Dingen irgendwas in eine Datei schreibt. 
# Da braucht man ja dann keinen Rückgabewert
x=mach_was()
print(x)