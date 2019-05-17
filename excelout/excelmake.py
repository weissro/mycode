#!/usr/bin/env python3

import pyexcel

#def get_column():
    #input_a = input("\nWhat is the IP Address? ")
    #input_b = input("\nWhat is the driver associated with this device? ")
    #cola = input("What is the first colum you would like to create ?")
    #colb = input("What is the second colum you would like to create ?")
    #colc = input("What is the third column you would like to create ?")
    #cold = input("What is the fourth column you would like to create ?")
    #return cola,colb,colc,cold


def get_ip_data(a,b,c,d):
    first = a
    second = b
    third = c
    fourth = d
    firstinp = input(f"\nWhat would you like to put in {first}? ")
    secondinp = input(f"\nWhat would you like to put in {second} ?")
    thirdinp = input(f"\nWhat would you like to put in {third} ?")
    fourthinp = input(f"\nWhat would you like to put in {fourth} ?")
    d = {first: firstinp, second: secondinp, third: thirdinp, fourth: fourthinp}
    return d

def main():
    mylistdict = []
    print("Hello!  This program will make you a *.xls file")
    cola = input("\nWhat is the first column you'd like to create? ")
    colb = input("\nWhat is the second column you'd like to create? ")
    colc = input("\nwhat is the third column you'd like to create? ")
    cold = input("\nWhat is the fourth column you'd like to create? ")

    while(True):
        mylistdict.append(get_ip_data(cola,colb,colc,cold))
        keep_going = input("\nWould you like to add another value? Enter to continue or enter 'q' to quit. ")
        if (keep_going.lower() == "q"):
            break

    filename = input("\nWhat is the name of the *.xls file? ")
    pyexcel.save_as(records=mylistdict, dest_file_name=filename +".xls")
    print("The file "   + filename + " .xls should be in your local directory")

main()
