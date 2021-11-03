#!/usr/bin/env python3

a = 5
b = 0

# Arithmetik
a = a + 123
print(a)
a += 123
print(a)

b = 5 ** 3
print(b)

a = 7
print(b / a)
print(b % a)
print(b // a)
print((b % a) / a)

# Vergleich
print(a > b)
print(a < b)

# Logik
print("A\t\tB\t\tNot A\t\tNot B\t\tA and B\t\tA or B")
print("-" * 100)
for a in True, False, None:
    for b in True, False, None:
        print(a, b, not a, not b, a and b, a or b, sep="\t\t")
    print("-" * 100)
