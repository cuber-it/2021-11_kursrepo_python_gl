#!/usr/bin/env python3

ip=input("IP eingeben: ")
while ip.lower() != "exit":
    
    if ":" in ip:
        port_index=ip.index(":")
        port_begin=port_index+1
        print("Port auslesen: ", ip[port_begin:])
        if ip[:port_index] == "127.0.0.1":
            print("loopback?"," Ja")
        else: 
            print("loopback?"," nein")
        ip1,ip2,ip3,ip4=ip.split('.')
        ip5,port=ip4.split(":")
        if int(ip1)>0 and int(ip1)<255:
            print("ip1 gültig!")
        else:
            print("ip1 nicht gültig!")
        if int(ip2)>0 and int(ip2)<255:
            print("ip2 gültig!")
        else:
            print("ip2 nicht gültig!")
        if int(ip3)>0 and int(ip3)<255:
            print("ip3 gültig!")
        else:
            print("ip3 nicht gültig!")
        if int(ip5)>0 and int(ip5)<255:
            print("ip4 gültig!")
        else:
            print("ip4 nicht gültig!")
    

    else:
        print("no port gegeben")
        if ip == "127.0.0.1":
            print("loopback?"," Ja")
        else: 
            print("loopback?"," nein")

        ip1,ip2,ip3,ip4=ip.split('.')
     
        if int(ip1)>0 and int(ip1)<255:
            print("ip1 gültig!")
        else:
            print("ip1 nicht gültig!")
        if int(ip2)>0 and int(ip2)<255:
            print("ip2 gültig!")
        else:
            print("ip2 nicht gültig!")
        if int(ip3)>0 and int(ip3)<255:
            print("ip3 gültig!")
        else:
            print("ip3 nicht gültig!")
        if int(ip4)>0 and int(ip4)<255:
            print("ip4 gültig!")
        else:
            print("ip4 nicht gültig!")
    ip=input("IP eingeben: ")

