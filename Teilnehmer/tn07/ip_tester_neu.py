#!/usr/bin/env python3
import sys
import os

loopback_ip = "127.0.0.1"
eingabe = ""

while eingabe.lower() != "exit": 
    eingabe = input("IP-Adresse eingeben: (xxx.xxx.xxx.xxx:yyyyyy)\n")
    if eingabe.lower() != "exit":
        if ":" in eingabe:
            ip = eingabe[:eingabe.index(":")]
            port = eingabe[eingabe.index(":")+1:]
            print("IP-Adresse: ",ip)
            print("Port: ",port)
        else:
            ip = eingabe
            print("IP-Adresse: ",ip)
        if ip == loopback_ip:
            print("WARNUNG: Loopback! Angegebene IP-Adresse nicht gültig.")
        else:
            ip_1, ip_2, ip_3, ip_4 = ip.split(".")
            ip_1 = int(ip_1)
            ip_2 = int(ip_2)
            ip_3 = int(ip_3)
            ip_4 = int(ip_4)
