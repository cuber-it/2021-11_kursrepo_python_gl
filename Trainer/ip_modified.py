ip_adresse = "123.123.123.1:8080"

position_doppelpunkt = ip_adresse.index(":")
port_beginn = position_doppelpunkt + 1
port = ip_adresse[port_beginn:]
print(port)

ip_adresse_1, ip_adresse_2, ip_adresse_3, ip_adresse_4 = ip_adresse[:position_doppelpunkt].split(".")
print(ip_adresse_1)
print(ip_adresse_2)
print(ip_adresse_3)
print(ip_adresse_4)

p1 = ip_adresse.index(".")
p2 = ip_adresse.index(".", p1+1)
p3 = ip_adresse.index(".", p2+1)

print(p1)
print(p2)
print(p3)