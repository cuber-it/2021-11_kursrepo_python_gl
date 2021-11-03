print("Dieses Programm führt Grundrechenarten durch.")
print("Bitte geben Sie zwei Ganzzahlen und die Rechenfunktion in die Eingabefelder ein")
z1 = input("Eingabe Zahl 1: ")
if z1.isdigit():
  print("Sie haben eine Zahl eingegeben")
else:
     z1 = input("Eingabe Zahl 1: ")
z2 = input("Eingabe Zahl 2: ")
calc = input("bitte geben Sie addm sub, mur oder div ein ")
if z1.isdigit() and z2.isdigit():
    print("Sie haben die Zahlen richtig eingegeben")
    zahl1=int(z1)
    zahl2=int(z2)
    if calc == "add":
     Ergebnis = zahl1 + zahl2
     print(Ergebnis)
    elif calc == "sub":
     Ergebnis = zahl1 - zahl2
     print(Ergebnis)
    elif calc == "mul":
     Ergebnis = zahl1 * zahl2
     print(Ergebnis) 
    elif calc == "div":
     Ergebnis = zahl1 // zahl2
     Rest = zahl1 % zahl2
     print(Ergebnis, Rest)  