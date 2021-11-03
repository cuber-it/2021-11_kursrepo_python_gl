#!/usr/bin/env python3

eingabe=""
while True:
    eingabe=input("Eingeben 6 Zahlen zwischen 1-49: ")
    if eingabe.lower()=="exit":
        break
    L1 = eingabe.split(",")
    if len(L1) != 6:
        print("Anzahl nicht richtig")
    else:
        nd=[]
        
        for i in range(0,len(L1)):
            if not L1[i].isdigit():
                nd.append(i)
        if len(nd)!=0:
            print("index {} not digit".format(nd))
        else:
            nn=[]
            for i in range(0,len(L1)):
                if int(L1[i]) < 1 or int(L1[i]) > 49:
                    nn.append(i)
            if len(nn)!=0:
                
                print("index {} not in 1-49".format(nn))  
            else:
                if len(set(L1))!=len(L1):
                    print("Es gibt doppelt")