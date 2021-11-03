#!/usr/bin/env python3
import sys
import os

#ip="127.0.0.1:8081"

ip=input("Bitte geben Sie eine IP-Adresse oder exit: ")
while ip.lower() != "exit":
    ip_parts=ip.split(":")
    #print(len(ip_parts))
    if(len(ip_parts) < 1 or len(ip_parts) > 2):
        print("Es handelt sich nicht um eine gültige Adresse")
    else:
        if(len(ip_parts)==2):
            print(f"Der Port ist: {ip_parts[1]}")
        if(ip_parts[0]=="127.0.0.1"):
            print("Es handelt sich um den Loopback 127.0.0.1")
        ip_subparts=ip_parts[0].split(".")
        if(len(ip_subparts)==4):
            ip_1,ip_2,ip_3,ip_4=ip_parts[0].split(".")
            if(ip_1.isdigit() and ip_2.isdigit() and ip_3.isdigit() and ip_4.isdigit()):
                if((int(ip_1) and int(ip_2) and int(ip_3) and int(ip_4))>=0 and (int(ip_1) and int(ip_2) and int(ip_3) and int(ip_4))<256):
                    print("die IP Adresse ist gültig.")
    ip=input("Bitte geben Sie eine IP-Adresse oder exit: ")

