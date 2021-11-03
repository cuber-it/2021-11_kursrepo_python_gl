#!/usr/bin/env python3
import sys
import os

def do_something(value):
    print(f"{value}")

def my_calculation(a, b):
    if b < 0:
        raise "Zero Value!"
    result = a / b
    return result


do_something("Hello")
c = my_calculation(2, 3)
print(f"Ergebnis: {c}")