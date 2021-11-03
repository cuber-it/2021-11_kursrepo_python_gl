#! /usr/bin/env python3
import random

def mach_was():
    result = random.sample(range(1,50), 6)
    result2 = random.sample(range(1,50), 6)
    return result, result2

x, y = mach_was()

print(*x)
print(*y)