#!/usr/bin/env python3
var = 4711
print(type(var), var)
var = "Hello" # oder var = 'Hello'
print(type(var), var)
var = 12.34e5 # 12,35 mal 10 hoch 5
print(type(var), var)
var = None # Nichts
print(type(var), var)
var = [1,2,3] # Liste
print(type(var), var)
var = (1,2,3) # Tuple
print(type(var), var)
var = {"a":1, "b":2, "c":3} # Dictionary
print(type(var), var)

x = var # x zeigt jetzt auch auf das Dictionary aus Zeile 14!!

print(dir())
del var # löscht den Namen, aber x zeigt noch auf das Dict, Daten bleiben erhalten
print(dir())

print(type(x), x) 
del x # nun zeigt nichts mehr auf das Dict - die Daten werden nun auch gelöscht