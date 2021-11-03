#!/usr/bin/env python3
#!/usr/bin/env python3
import random

def lese_tipp():
    ergebnis = []
    count = 0
    while count < 6:
        try:
            zahl = int(input("Eine Zahl: "))
            if zahl < 1 or zahl > 49:
                print("ungültige zahl")
            elif zahl in ergebnis:
                print("doppelte zahl")
            else:
                ergebnis.append(zahl)
                count += 1
        except:
            print("Das war wohl nix!")
    ergebnis.sort()
    return ergebnis

def erzeuge_ziehung(max_numbers=6, min_val=1, max_val=49):
    ergebnis = random.sample(range(min_val, max_val+1),k=max_numbers)
    ergebnis.sort()
    return ergebnis

def werte_spiel_aus(tipp, ziehung):
    return len(list(set(ziehung) & set(tipp)))

def gebe_ergebnis_aus(ergebnis):
    print("Treffer", ergebnis)

#--- Hauptprogrammteil, wird aufgerufen, wenn diese Datei direkt gestartet wird
# beim import wird der Code nicht ausgeführt
if __name__ == "__main__":
    tipp = lese_tipp()
    ziehung = erzeuge_ziehung()
    ergebnis = werte_spiel_aus(tipp, ziehung)
    gebe_ergebnis_aus(ergebnis)