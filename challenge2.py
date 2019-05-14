#!/usr/bin/env python3

first_list = []
switch = {"first_name" : "Monty", "last_name" : "Python", "actions" : ["Scooter", 2, "Moscow"]}

print(f"In {(switch['first_name'])} {(switch['last_name'])}, Eric Idle rode a {(switch['actions'][0])} {(switch['actions'][1])} {(switch['actions'][2])}")
#first_list.append("horse")
#first_list.append("to") 
#first_list.append("the Holy Grail")
## could have used first_list.append() or first_list.extend()
first_list.append("horse")
first_list.extend(["to", "the Holy Grail"])
# or create a second list and first_list.extend(second_list)
switch["actions"] = first_list
print(switch)
print(f"In {(switch['first_name'])} {(switch['last_name'])}, Eric Idle rode a {(switch['actions'][0])} {(switch['actions'][1])} {(switch['actions'][2])}")

