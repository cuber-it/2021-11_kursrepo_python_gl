#!/usr/bin/env python3

bmi = 32.123456

print(f"Der BMI ist: {bmi:.1}")
print(f"Der BMI ist: {bmi:.1f}")

s1 = "Hello"
s2 = "world"

# Reine Ausgaben!!!
print(s1, s2) # Hintereinanderausgabe mit default Leerzeichen
print(s1, s2, sep=":") # Hintereinanderausgabe mit :-Zeichen



print(s1 + s2) # Concatenation
s3 = s1 + s2
print(s3)

s3 = ":".join([s1, s2]) # Baut String aus den Worten in der Liste mit dem angeg. Trennzeichen
print("S3: ", s3)

print(s1 * 5) # Stringmultiplikation
print(s1 + str(21)) # Crasht da Typen inkompatibel für Operation, daher vorher Umwandlung der Zahl in String

