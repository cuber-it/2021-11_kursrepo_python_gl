#!/usr/bin/env python3

# ip = "127.0.0.1:113" # noch als Eingabe auszuführen


while True:
    ip = input("IP: ")
    if ip != "exit":
        if ":" in ip:
            position_doppelpunkt = ip.index(":")
            port = ip[position_doppelpunkt + 1:]
            ip = ip[0:position_doppelpunkt]
            ip_1, ip_2, ip_3, ip_4 = ip[:position_doppelpunkt].split(".")
            print("Port: " + port)
        else:
            ip_1, ip_2, ip_3, ip_4 = ip.split(".")
        if ip == "127.0.0.1":
            print("IP ist Loopback")
        if int(ip_1) <= 255 and int(ip_2) <= 255 and int(ip_3) <= 255 and int(ip_4) <= 255:
            print("IP ist gültig")
        else:
            print("IP ist ungültig")
    else:
        break