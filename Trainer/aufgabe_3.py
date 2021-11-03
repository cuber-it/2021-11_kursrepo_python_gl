#!/usr/bin/env python3
while True:
    eingabe = input("IP- mit optionalem Port: ").lower() # Normalisierung der eingabe um es besser testen zu können
    if eingabe == "exit":
        break
    if ":" in eingabe:
        position = eingabe.index(":")
        print("Port: ", eingabe[position+1:])
        ip = eingabe[:position]
    else: 
        ip = eingabe

    if ip == "127.0.0.1":
        print("Loopback!")
    else:
        p1 = ip.index(".")
        ip1 = int(ip[:p1])
        p2 = ip.find(".", p1+1)
        ip2 = int(ip[p1+1:p2])
        p3 = ip.index(".", p2+1)
        ip3 = int(ip[p2+1:p3])
        ip4 = int(ip[p3+1:])
        
        if ip1 < 0 or ip1 > 255:
            print(f"Teiladresse 1 nicht in Ordnung {ip1}")
        else:
            print("Teiladresse 1 in Ordnung")

        if ip2 < 0 or ip2 > 255:
            print(f"Teiladresse 2 nicht in Ordnung {ip2}")
        else:
            print("Teiladresse 2 in Ordnung")

        if ip3 < 0 or ip3 > 255:
            print(f"Teiladresse 3 nicht in Ordnung {ip3}")
        else:
            print("Teiladresse 3 in Ordnung")

        if ip4 < 0 or ip4 > 255:
            print(f"Teiladresse 4 nicht in Ordnung {ip4}")
        else:
            print("Teiladresse 4 in Ordnung")

        # in der echten Welt:
        faulty = []
        tripletts = ip.split(".")
        for triplet in tripletts:
            if not (0 <= int(triplet) <= 255):
                faulty.append(triplet)
        if len(faulty) > 0:
            print(f"Die waren nicht korrekt {faulty}")

