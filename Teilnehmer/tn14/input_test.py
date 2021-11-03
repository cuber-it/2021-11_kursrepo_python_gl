#!/usr/bin/env/ python3
import sys
import os

filename="/home/coder/Workspace/aktueller-kurs/Materialien/sample.log.txt"
f=open(filename,"r")
lc=0 # linecount
n_event=0
n_info=0
for x in f:
    filecontent=f.readline()
    # print(filecontent)
    lc=lc+1
    if filecontent.find("EVENT") != -1:
        i_events=x
        n_event=n_event+1
    if filecontent.find("INFO") != -1:
        i_info=x
        n_info=n_info+1
f.close()
print("Lines",lc)
print("#EVENT",n_event)
print("#INFO",n_info)
print(type(filecontent))
print(filecontent)