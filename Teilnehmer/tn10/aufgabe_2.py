#!/usr/bin/env python3
import sys
import os

ip = "198.10.128.3:8080"
loopback = "127.0.0.1"


eingabe = input("Texteingabe: ")
while eingabe != "exit":
  if ip.find(":"):
    pos_doppelpunkt = ip.index(":")
    pos_port = pos_doppelpunkt + 1
    port = ip[pos_port:]
    print(port)
  else:
    print("Kein Port angegben")

  if ip == loopback:
    print("Es wurde die Loopback-Adresse ", loopback, " angegeben")


  eingabe = "exit"