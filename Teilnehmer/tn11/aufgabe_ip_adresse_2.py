#!/usr/bin/env python3
import sys
import os

#ip="127.0.0.1:8081"

ip=input("Bitte geben Sie eine IP-Adresse oder exit: ")
while ip.lower() != "exit":
    ip_parts=ip.split(":")
    if(len(ip_parts) < 1 or len(ip_parts) > 2):
        print("Es handelt sich nicht um eine gültige Adresse")
    else:
        if(len(ip_parts)==2):
            print(f"Der Port ist: {ip_parts[1]}")
        if(ip_parts[0]=="127.0.0.1"):
            print("Es handelt sich um den Loopback 127.0.0.1")
        ip_subparts=ip_parts[0].split(".")
        if(len(ip_subparts)==4):
            for digits in ip_subparts:
                if digits.isdigit() and int(digits) >= 0 and int(digits)<256:
                    print(f"Die Zahl {digits} gültig.")
                else:
                    print(f"Die Zahl {digits} ist ungültig.")
    ip=input("Bitte geben Sie eine IP-Adresse oder exit: ")

