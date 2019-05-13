#!/usr/bin/env python3

# the key  is important in order to find the value.  Require you to know what key is
first_dictionary = {}
second = {"car": "malibu", "dream_car": "corvette"} 
print(second["car"])
print(second["dream_car"])
second.update({"dream_car" : "bugatti"})
print(second)

# another way of updating a key value
second["car"] = ["prius" , "gremlin", "saturn"]
print(second)
print(second["car"][1])
#print(second.values())
