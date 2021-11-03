eingabe = input("Bitte geben Sie 6 unterschiedliche Zahlen aus 49 kommagetrennt ein: ")

zahlen = eingabe.replace(" ","").split(",")

print(zahlen)
tipp = []
if len(zahlen) != 6:
    print("Falsche Anzahl Zahlen")
    tipp = "Abbruch"
    exit()

else:
    for n in zahlen:      
        zahl = int(n)                   
        if zahl < 1 or zahl > 49:
            print("Keine Zahl zwischen 1 und 49")
        if zahl in tipp:
            print("Tipp doppelt abgegeben")
            tipp = "Abbruch"
        else: 
            tipp.append(zahl)
                  
        
print(tipp)