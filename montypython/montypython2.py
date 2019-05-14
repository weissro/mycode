#!/usr/bin/env python3

round = 0

while(True):
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input()
    if (answer.upper() == 'BRIAN'):
        print('Correct')
        break
    elif(round==3):
        print('Sorry, the answer was Brian.')
        break
    elif(answer.upper() == "SHRUBBERY"):
        print('You gave the super secret answer so you win anyhow!')
        break
    else: 
        print("Sorry, try again.")

