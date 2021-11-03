#!/usr/bin/env python3
import sys
import os

ip = "123.123.12.1:5432"
ip_loopback = "127.0.0.1"
eingabe = ""



while eingabe.lower != "exit": 
    eingabe = input("zum Beenden 'exit' eingeben\n")
    port = ip[ip.index(":")+1:]
    print(port)
    if ip_loopback in ip: 
        print("WARNUNG: IP-Adresse ist die Loopback-Adresse")
    ip_1, ip_2, ip_3, ip_4 = eingabe[:eingabe.index(":")].split(".")
    ip_1 = int(ip_1)
    ip_2 = int(ip_2)
    ip_3 = int(ip_3)
    ip_4 = int(ip_4)
    if ip_1 or ip_2 or ip_3 or ip_4 > 256:
        print("WARNUNG: Keine gültige IP-Adresse!")
