#!/usr/bin/env python3
import sys
import os
import math


loopback = "127.0.0.1"
ip = " "
while ip.lower != "exit" :
      ip = input("Eingabe IP:  ")
      if ip == "exit":
         exit()
      pos_doppelpkt = ip.index(":")
   
      doppelpunkt = True
      if doppelpunkt is True :
         port_start = pos_doppelpkt + 1
         port = ip[port_start:]
         print ((" Port: ") + port)

      if  loopback  in ip :
          print (loopback + " ist enthalten")

      p1 = ip.index(".")
      p2 = ip.index(".", p1+1)
      p3 = ip.index(".", p2+1)

      w1 = int(ip[:p1])
      w2 = int(ip[p1+1:p2])
      w3 = int(ip[p2+1:p3])
      w4 = int(ip[p3+1:pos_doppelpkt])
   

      if w1 > 0 and w1 < 255 :
          print (w1)
      if w2 >= 0 and w2 < 255 :
          print (w2)
      if w3 >= 0 and w3 < 255 :  
          print (w3)
      if w4 > 0 and  w4 < 255 :  
          print (w4)   


      

