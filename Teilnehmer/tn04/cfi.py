a=input("first interger number: ")
b=input("second interger number: ")
c=input("choose one mathematical operation from add=addition, sub=substraction, mul = multiplication, div=division: ")
if a.isdigit() and b.isdigit():
    a=int(a)
    b=int(b)
    if c == "add":
        d=a+b
        print("The result is: ",d)
    elif c =="sub":
        d=a-b
        print("The result is: ",d)
    elif c =="mul":
        d=a*b
        print("The result is: ",d)
    elif c =="div":
        d1 = a//b
        d2 = a%b
        print("The result is: ",d1, "modulo", d2)
    else:
        print("No valid operator was given.")
else:
    print("Die Entry is invalid.")

#Interesting... whenever one needs the code to stop, use exit()



