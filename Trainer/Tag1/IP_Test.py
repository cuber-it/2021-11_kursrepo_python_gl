

eingabe = ""

while eingabe.lower() != "exit":
    eingabe = input("IP- optionalen Port: ")
    if eingabe.lower() != " exit":
            
position_doppelpunkt = ip.index(":")
port_beginn = position_doppelpunkt +1
port = ip[port_beginn:]
print (port)
ip_1, ip_2, ip_3, ip_4 = ip[:position_doppelpunkt].split(".")
print(ip_1)
print(ip_2)
print(ip_3)
print(ip_4)

p1 = ip.index(".")
p2 = ip.index(".", p1+1)
p3 = ip.index(".", p2+1)

print(p1)
print(p2)
print(p3)
#p1 = ip.index(".") p2 = ip.index(".", p1+1) p3 = ip.index(".", p2+1) print(p1) print(p2) print(p3)