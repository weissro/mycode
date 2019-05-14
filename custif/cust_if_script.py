#!/usr/bin/env python3

print("What grade did you get on your test?")
grade = float(input())

if grade >= 90 and grade <= 100:
    print("Great job!  You got an A!")

elif grade >= 80 and grade < 90:
    print("Nothing wrong with a B")

elif grade >= 70 and grade < 79:
    print("C is average.  You should study more.")

elif grade >= 60 and grade < 69:
    print("Eww.  A D?  Not good at all.  Work harder.")

elif grade >= 0 and grade < 59:
    print("You failed.  Hit the books!")

else:
    print("Grades are 0-100.  Try inputting it again.")



