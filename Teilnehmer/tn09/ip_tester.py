#!/usr/bin/env python3
import sys
import os

ip = "12.14.15.288:88" # 'for testing'


ip = "dummy"
while ip != 'exit':   #  oder while True und dann nach eingabe : If IP == exit: break
    ip = input("Please enter IP-Adress:").lower()
    if ip != "exit":
        if ':' in ip:
            position_doppelpunkt = ip.index(":")
            #print(position_doppelpunkt)
            port = ip[position_doppelpunkt+1:]
            print("Port: ", port)
            ip = ip[:position_doppelpunkt]
        else: print("No Port is given")


        loopback = "127.0.0.1"
        if loopback in ip: print("Die IP-Adresse ist gleich der loopback-Adresse")

        triplets = ip.split(".")
        #print("triplets",triplets)

        not_valid = []
        for triplet_i in triplets:
            if not (0<= int(triplet_i) <=255):
                not_valid.append(int(triplet_i))
        if len(not_valid) > 0: print("invalid IP-Values: ",  not_valid)

    
