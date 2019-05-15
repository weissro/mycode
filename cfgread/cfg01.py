#!/usr/bin/env python3

######Explore read ######
##create file object in "r"ead mode

configfile = open("vlanconfig.cfg", "r")

#display file to the screen - .read()
print(configfile.read())

##close the file
configfile.close()

###explore readlines
##re-create file object to explore new method

configfile = open("vlanconfig.cfg", "r")

##make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## iterate through configlist
for x in configlist:
    print(x)

configfile.close()

