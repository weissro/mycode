#!/usr/bin/env python3

#open file
dnsfile = open("dnsservers.txt")
#create list of lines
dnslist = dnsfile.readlines()
#loop over lines
for svr in dnslist:
    #print and end without a new line
    print(svr,end="")

#close file
dnsfile.close()


