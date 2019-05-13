#!/usr/bin/en python3

mylist = ["cat", "dog", 7]
#print(mylist[1])

print(f"I have a {mylist[0]} and a {mylist[1]} that are {mylist[2]}.")
mylist.append("hamster")
mylist.extend("hamster")
print(mylist.pop())
print(mylist)


