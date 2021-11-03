#!/usr/bin/env/ python3
import sys
import os
#Eingabe
ip_in=""

while ip_in != "q":
    ip_in=input("EingabeIPAdresse ? (for Exit = q): ")
    print("eingegebene IP",ip_in)
    position_doppelpunkt=ip_in.find(":")
    # print("Position Doppelpunkt",position_doppelpunkt)
    if ip_in.startswith("127.0.0.1"):
        print("LoopBackIP!!!")
    if position_doppelpunkt != -1:    
        print("Port specified @ ",position_doppelpunkt)
        ip_1, ip_2, ip_3, ip_4 = ip_in[:position_doppelpunkt].split(".")
        print("P1p",ip_1)
        print("P2p",ip_2)
        print("P3p",ip_3)
        print("P4p",ip_4)
        print("PortNumber",ip_in[position_doppelpunkt+1:])
        ip_sub=ip_in[:position_doppelpunkt]
        #print("ip_sub=",ip_sub)
    else:
        print("No Port specified")
        ip_1, ip_2, ip_3, ip_4 = ip_in[:].split(".")
        print("P1",ip_1)
        print("P2",ip_2)
        print("P3",ip_3)
        print("P4",ip_4)
        ip_sub=ip_in
    ip1, ip2, ip3, ip4 = (ip_sub[:].split("."))
    if int(ip1) < 0 or int(ip1) > 255:
       print("1. Triplet invalid",ip1)
    if int(ip2) < 0 or int(ip2) > 255:
       print("2. Triplet invalid",ip2)
    if int(ip3) < 0 or int(ip3) > 255:
       print("3. Triplet invalid",ip3)
    if int(ip4) < 0 or int(ip4) > 255:
       print("4. Triplet invalid",ip4)