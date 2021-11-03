lottozahlen = []

while len(lottozahlen) <=5 :
    number = input("Choose a number between 1 and 49: ")
    if number.isdigit():
        number=int(number)
        if number >= 1 and number <= 49:
            if number not in lottozahlen:
                lottozahlen.append(number)
            else: 
                print("Something went wrong.")
        else: 
            print("Something went wrong.")
    else: 
        print("Something went wrong.")
    
    

print("Entry of you lottery numbers was successful.")
print(lottozahlen)
