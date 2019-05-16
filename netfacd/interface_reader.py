#!/usr/bin/env python3

import netifaces
print(netifaces.interfaces())

for i in netifaces.interfaces():
    print("******* Details of Interface - " + i + "***************")
    try:  
        # this is a new line.  You also have to indent the code below
        print("MAC: ", end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]["addr"]) # prints the mac address
        print("IP: ", end='')
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]["addr"]) # prints the IP address
    except:
        print("Could not collect adapter information.") # Error handler
    
    


