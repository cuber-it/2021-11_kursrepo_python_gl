while True:
 ip_addr = input("Bitte geben Sie eine gültige IP-Adresse ein: ")
 pport1 = ip_addr.find(":")
 if pport1 == -1:
  print("Kein Port angegeben")
 else: 
  pport = ip_addr[pport1+1:]
  print(pport)
 if ip_addr.lower() == "exit":
   break