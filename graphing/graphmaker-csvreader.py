#!/usr/bin/env python3

import csv

import numpy as np
import matplotlib.pyplot as plt

def parsecsvdata():
    """returns a list.  [0] is LAN, [1] is WAN"""
    summary = [] # a list that will contain LAN and WAN

    #open CSV data
    with open("/home/student/mycode/graphing/2018summary.csv", "r") as downtime:
            # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (int(row[0]), int(row[1]), int(row[2]), int(row[3]))
            summary.append(rowdat) # add dict to list
    return summary

def main():
    N = 4
    ## grab our data
    summary = parsecsvdata() # grab out data
    localnetMeans = summary[0] # LAN data
    wanMeans = summary[1] # WAN data

    ind = np.arange(N)
    width = 0.35

    p1 = plt.bar(ind, localnetMeans, width)
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    plt.ylabel("Length of Outage (Mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    plt.savefig\
            ("/home/student/mycode/graphing/2018bsummary.png")
    plt.show()
    print("Graph created")


main()
        
