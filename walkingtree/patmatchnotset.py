#!/usr/bin/env python3

import os
import fnmatch

EXCLUDE = ["/usr", "home", "/var"] # do not search in these locations

def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files, in os.walk(path,topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] #remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: #always perform the nested loop but it may be empty
            if fnmatch.fnmatch(name, pattern): # if match
                result.append(os.path.join(root,name))
    return result

def main():
    lookfor = input("What pattern am I looking for (example *.py)? ")
    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", find(lookfor,lookwhere)) 


main()



