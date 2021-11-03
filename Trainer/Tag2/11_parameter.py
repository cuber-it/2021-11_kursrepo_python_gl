#!/usr/bin/env python3
def f1():
    print("f1")

f1()
# f1("HUHU") gibt Exception

def f2(p):
   print("f2", p) 

def f3(p, o=1):
   print("f3", p, o) 

def f4(p, *a): # (1), ("a", 1) ... (1,2,3,4,5,6,7,8,9)
   print("f4", p, a) 

def f5(p, **k): # (1), ("a", x=123) ... (1, x=123, b=345, ....)
   print("f5", p, k) 

def f6(p, o=1, *a, **k): # sowas sieht man z.B. in der CSV-Bibliothek :-D
   print("f6", p, o, a, k) 

# Exception f2()
f2(1234)
f2(p=1234)
# Exception f2(12, 34, 56)

f3(1)
f3(1, 2)
f3(o=9, p=7)
# Exception f3(1, 2, 3)

f4(1)
f4(1, 2)
f4(1, 2, 3)
f4(1, 2, 3, 4, 5)

f5(1)
f5(1, name="Willi")
f5(1, name="Willi", ort="Watzingen")

f6(1, 99, 3, 4, 5, my_val=1, your_val="Hallo")

