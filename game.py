
from ast import Break
import random

l2=["ROCK","PAPER","SCISSOR"]
warn=("CHOOSE A COMMAND FROM THE ABOVE LIST!")
print(l2)
print(warn)

A=input("Please Select Your Option:")


#if you choose rock as option
if A =="ROCK":
    rand= random.choice(l2)
    print("I chose:",rand)
    if rand=="PAPER":
        print("I WON")
    elif rand=="ROCK":
        print("MATCH IS DRAW")
    else:
        print("YOU WON")    
else:
    Break

#if you choose paper as option
if A =="PAPER":
    rand= random.choice(l2)
    print("I chose:",rand)
    if rand=="SCISSOR":
        print("I WON")
    elif rand=="PAPER":
        print("MATCH IS DRAW")
    else:
        print("YOU WON")    
else:
    Break 

#if you choose scisor as option
if A =="SCISSOR":
    rand= random.choice(l2)
    print("I chose:",rand)
    if rand=="ROCK":
        print("I WON")
    elif rand=="SCISSOR":
        print("MATCH IS DRAW")
    else:
        print("You Won")
else:
    Break


