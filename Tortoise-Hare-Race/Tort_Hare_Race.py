# Assignemtn 2, Question 4
# Created by Natalia Wilson
# Recreate the classic race of the tortoise and the hare.

import random
tortoisePos = 0
harePos = 0

def tortoiseProb():
    randomNum = random.randint(1,10)
    #if number is in range 1-5 it is a fast plod
    if(randomNum in range(1,6)):
        return 3
    #if number is 6 or 7 the tortoise slips
    elif(randomNum in range(6,8)):
        return -6
    #if number is 8,9 or 10 the tortoise slow prods
    else:
        return 1

def hareProb():
    randomNum = random.randint(1,10)
    #if number is in range 1-3 the hare sleeps
    if(randomNum in range(1,3)):
        return 0
    #if number is 3 or 4 the hare big hops
    elif(randomNum in range(3,5)):
        return 9
    #if number is 5 the hare big slips
    elif(randomNum == 5):
        return -12
    #if number is 6,7 or 8 the hare small hops
    elif(randomNum in range(6,9)):
        return 1
    #if number is 9 or 10 the tortoise small slips
    else:
        return -2

#start of the game
print("BANG! AND THEY'RE OFF!")
tortWinCount = 0
hareWinCount = 0
gameCount = 0
for i in range(10):
    while(True):
        for i in range(75):
            #If hare and tort in same pos:
            if(tortoisePos==harePos and i == tortoisePos):
                print('OUCH!!',end='')
            else:
                #print tort(T) and hare(H) pos and race tracks (-):
                if(i==tortoisePos):
                    print('T',end='')
                elif(i==harePos):
                    print('H',end='')
                else:
                    print('-',end='')
        print()
        #tort or hare finishes race
        if(tortoisePos>=70 or harePos >=70):
            break
        #getting the moves for both after each loop
        tortoisePosMove = tortoiseProb()
        harePosMove = hareProb()
        tortoisePos = tortoisePos + tortoisePosMove
        harePos = harePos + harePosMove
        #if pos is neg then pos = 0
        if(tortoisePos < 0):
            tortoisePos = 0
        if(harePos < 0):
            harePos = 0

    #prints winner
    if(tortoisePos>harePos):
        print('TORTOISE WINS! YAY!')
        tortWinCount += 1
        gameCount += 1
        tortoisePos = 0
        harePos = 0
    elif(tortoisePos<harePos):
        print('Hare wins')
        hareWinCount += 1
        gameCount += 1
        tortoisePos = 0
        harePos = 0
    else:
        print("It's a tie")
        tortoisePos = 0
        gameCount += 1
        harePos = 0
print()
print(f'Tortoise Wins   Hare Wins\n\
{tortWinCount}               {hareWinCount}')