wrong=0
ip_input=input("Please enter IP address: ")
while ip_input != "exit":
    
    if "127.0.0.1" in ip_input:
        print("Loopback detected!")

    if ":" in ip_input:
        ip_port= ip_input.split(":")
        ip=ip_port[0]
        port=ip_port[1]
        
        triplets=ip.split(".")
        t1=int(triplets[0])
        t2=int(triplets[1])
        t3=int(triplets[2])
        t4=int(triplets[3])
        for i in [t1,t2,t3,t4]:
            if i >= 0 and i <= 255:
                wrong=wrong+0                
            else:
                wrong=wrong+1
        if wrong ==0:
            print("The given address contains the port number {}.".format(port))    
            print("All triplets {}, {}, {}, {}, of the IP address are valid.".format(t1,t2,t3,t4))
        else:
            print("The given address contains the port number {}.".format(port))  
            print("At least one of the triplets {}, {}, {}, {} of the given IP address is invalid.".format(t1,t2,t3,t4))
            
    else:
        triplets=ip_input.split(".")
        t1=int(triplets[0])
        t2=int(triplets[1])
        t3=int(triplets[2])
        t4=int(triplets[3])
        for i in [t1,t2,t3,t4]:
            if i >= 0 and i <= 255:
                wrong=wrong+0
            else:
                wrong=wrong+1
        if wrong ==0:
            print("The given address contains no port number.")    
            print("All triplets {}, {}, {}, {}, of the IP address are valid.".format(t1,t2,t3,t4))
        else:
            print("The given address contains no port number.")
            print("At least one of the triplets {}, {}, {}, {} of the given IP address is invalid.".format(t1,t2,t3,t4))

    ip_input=input("Please enter IP address: ")

