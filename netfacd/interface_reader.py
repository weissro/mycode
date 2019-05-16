#!/usr/bin/env python3

import netifaces
#print(netifaces.interfaces())


def ip_mac(selection):
    if (selection == "lo") or (selection == "ens3") or (selection == "docker0"):
        print("******* Details of Interface - " + selection + "***************")
        try:  
            # this is a new line.  You also have to indent the code below
            print("MAC: ", end='')
            print((netifaces.ifaddresses(selection)[netifaces.AF_LINK])[0]["addr"]) # prints the mac address
            print("IP: ", end='')
            print((netifaces.ifaddresses(selection)[netifaces.AF_INET])[0]["addr"]) # prints the IP address
        except:
            print("Could not collect adapter information.") # Error handler
    else:
            print("Sorry, that is not one of the interfaces.")


def main():
    which = input("Which interface do you want information on?  Pick lo, ens3, or docker0? :")

    ip_mac(which.lower())


main()

    


