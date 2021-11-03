#! /usr/bin/env python3

 # Testcases
#zahlen = "1, 2, 3, 4, 5, 6"
#zahlen = "1, 2, 3, 4, 500, 6"
#zahlen = "1, 2, 3, 4, 6"
#zahlen = "1, 2, 3, 4, 4, 6"
#zahlen = "1, 2, 3, 4, -5, 6"
#zahlen = "1, 2, 3, 4, A, 6"
zahlen = "exit"

#zahlen = input("6 Zahlen eingeben, keine Doppelten, mit Komma getrennt: ")
if zahlen != "exit":
    zahlen = zahlen.replace(" ","").split(",")
    if len(zahlen) != 6:
        print("Nicht 6 Zahlen eingegeben.")
        exit()
    for zahl in zahlen:
        if not zahl.isdigit():
            print(zahl + " ist keine positive Zahl.")
            exit()
        elif int(zahl) > 49:
            print(zahl + " ist größer als 49.")
            exit()
    if len(set(zahlen)) != 6:
        print("Doppelte Zahlen gefunden.")
        exit()
    print(*zahlen)
    print("Erfolg!")
else:
    print("Exit.")
