num1 = input("Gib die erste Zahl ein: ")
if num1.isdigit():
    print("Inhalt ist eine Ganzzahl")
else:
    exit()    
num2 = input("Gib die zweite Zahl ein: ")
if num2.isdigit():
    print("Inhalt ist eine Ganzzahl")
oper = input("Welche Rechenoperation soll durchgefuehrt werden? (add,sub,div,mul): ")

num1 = int(num1)
num2 = int(num2)

if oper == "add":
    print("Deine Rechnung:", num1, " + ", num2)
    print("Ergebnis:", num1 + num2)

elif oper == "sub":
    print("Deine Rechnung:", num1, " - ", num2)
    print("Ergebnis:", num1 - num2)
    
elif oper == "div":
    print("Deine Rechnung:", num1, " / ", num2)
    print("Ergebnis:", num1 / num2)
    
elif oper == "mul":
    print("Deine Rechnung:", num1, " * ", num2)
    print("Dein Ergebnis:", num1 * num2)
else:
    print("Deine Eingaben sind nicht gueltig")
