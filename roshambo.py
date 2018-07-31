# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:02:30 2018

@author: AdamF
"""

#rock paper scissors
import random
import time

enemies = ["Randy","Kyle","Fred","Bill","Anthony","Johnny Fingers","Hypno Toad","Samantha","Lisa","Petunia","Amelia","Jessica","Sarah 'Brains' Stompanato"]

print("Rock, Paper, Scissors! (v1)")
print("**********************")
pname = input("Enter your name! ")
pname = pname.capitalize()
again = "y"
proll = 0
victor = "None"
pscore = 0
oscore = 0
holdtime = random.randint(1,3)
minispacer = "          "
spacer = "                      "
prockg1 = "    _______          "
prockg2 = "---'   ____)         "
prockg3 = "      (_____)        "
prockg4 = "      (_____)        "
prockg5 = "      (____)         "
prockg6 = "---.__(___)          "
orockg1 = "          _______    "
orockg2 = "         (____   '---"
orockg3 = "        (_____)      "
orockg4 = "        (_____)      "
orockg5 = "         (____)      "
orockg6 = "          (___)__.---"
ppaperg1 = "     _______        "
ppaperg2 = "---'    ____)____   "
ppaperg3 = "           ______)  "
ppaperg4 = "          _______)  "
ppaperg5 = "         _______)   "
ppaperg6 = "---.__________)     "
opaperg1 = "        _______     "
opaperg2 = "   ____(____    '---"
opaperg3 = "  (______           "
opaperg4 = "  (_______          "
opaperg5 = "   (_______         "
opaperg6 = "     (__________.---"
pscissorg1 = "    _______       "
pscissorg2 = "---'   ____)____  "
pscissorg3 = "          ______) "
pscissorg4 = "       __________)"
pscissorg5 = "      (____)      "
pscissorg6 = "---.__(___)       "
oscissorg1 = "       _______    "
oscissorg2 = "  ____(____   '---"
oscissorg3 = " (______          "
oscissorg4 = " (______          "
oscissorg5 = "      (____)      "
oscissorg6 = "       (___)__.---"

while 1:
    opponent = (random.choice(enemies))
    if opponent != pname: #don't let computer name be the same as player's name
        break

print("Searching for an opponent",end="")
time.sleep(3)
for x in range(1,holdtime):
    print(" ...",end="")
    time.sleep(1)
print(" ... Found!")
time.sleep(1)
print("Your opponent's name is: ",opponent)
print("Let's play!")

while again != "n":
    while proll != 1 and proll !=2 and proll !=3:
        proll = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors.  Make your choice!  "))
        #proll = random.randint(1,3)
    #proll = 1
    oroll = random.randint(1,3)
    #oroll = 1
    print("Your roll: ",proll,"(",["Rock","Paper","Scissors"][proll-1],")                             ",end="")
    print("Opponent roll: ",oroll,"(",["Rock","Paper","Scissors"][oroll-1],")")
    #graphics time!
    if proll == 1: #rock
        if oroll == 1: #rock
            print(minispacer,prockg1,spacer,orockg1)
            print(minispacer,prockg2,spacer,orockg2)
            print(minispacer,prockg3,spacer,orockg3)
            print(minispacer,prockg4,spacer,orockg4)
            print(minispacer,prockg5,spacer,orockg5)
            print(minispacer,prockg6,spacer,orockg6)
        if oroll == 2: #paper
            print(minispacer,prockg1,spacer,opaperg1)
            print(minispacer,prockg2,spacer,opaperg2)
            print(minispacer,prockg3,spacer,opaperg3)
            print(minispacer,prockg4,spacer,opaperg4)
            print(minispacer,prockg5,spacer,opaperg5)
            print(minispacer,prockg6,spacer,opaperg6)
        if oroll == 3: #scissor
            print(minispacer,prockg1,spacer,oscissorg1)
            print(minispacer,prockg2,spacer,oscissorg2)
            print(minispacer,prockg3,spacer,oscissorg3)
            print(minispacer,prockg4,spacer,oscissorg4)
            print(minispacer,prockg5,spacer,oscissorg5)
            print(minispacer,prockg6,spacer,oscissorg6)
    if proll == 2: #paper
        if oroll == 1: #rock
            print(minispacer,ppaperg1,spacer,orockg1)
            print(minispacer,ppaperg2,spacer,orockg2)
            print(minispacer,ppaperg3,spacer,orockg3)
            print(minispacer,ppaperg4,spacer,orockg4)
            print(minispacer,ppaperg5,spacer,orockg5)
            print(minispacer,ppaperg6,spacer,orockg6)
        if oroll == 2: #paper
            print(minispacer,ppaperg1,spacer,opaperg1)
            print(minispacer,ppaperg2,spacer,opaperg2)
            print(minispacer,ppaperg3,spacer,opaperg3)
            print(minispacer,ppaperg4,spacer,opaperg4)
            print(minispacer,ppaperg5,spacer,opaperg5)
            print(minispacer,ppaperg6,spacer,opaperg6)
        if oroll == 3: #scissor
            print(minispacer,ppaperg1,spacer,oscissorg1)
            print(minispacer,ppaperg2,spacer,oscissorg2)
            print(minispacer,ppaperg3,spacer,oscissorg3)
            print(minispacer,ppaperg4,spacer,oscissorg4)
            print(minispacer,ppaperg5,spacer,oscissorg5)
            print(minispacer,ppaperg6,spacer,oscissorg6)
    if proll == 3: #scissor
        if oroll == 1: #rock
            print(minispacer,pscissorg1,spacer,orockg1)
            print(minispacer,pscissorg2,spacer,orockg2)
            print(minispacer,pscissorg3,spacer,orockg3)
            print(minispacer,pscissorg4,spacer,orockg4)
            print(minispacer,pscissorg5,spacer,orockg5)
            print(minispacer,pscissorg6,spacer,orockg6)
        if oroll == 2: #paper
            print(minispacer,pscissorg1,spacer,opaperg1)
            print(minispacer,pscissorg2,spacer,opaperg2)
            print(minispacer,pscissorg3,spacer,opaperg3)
            print(minispacer,pscissorg4,spacer,opaperg4)
            print(minispacer,pscissorg5,spacer,opaperg5)
            print(minispacer,pscissorg6,spacer,opaperg6)
        if oroll == 3: #scissor
            print(minispacer,pscissorg1,spacer,oscissorg1)
            print(minispacer,pscissorg2,spacer,oscissorg2)
            print(minispacer,pscissorg3,spacer,oscissorg3)
            print(minispacer,pscissorg4,spacer,oscissorg4)
            print(minispacer,pscissorg5,spacer,oscissorg5)
            print(minispacer,pscissorg6,spacer,oscissorg6)
            
    #check for winner!
    if proll-oroll == 0:
        print("It's a tie!")
    elif (proll-oroll+5)%3 == 0:
        print("You won!")
        pscore = pscore + 1
    else:
        print(opponent," won!")
        oscore = oscore + 1
        
    #score update!        
    print("***   Score update!   ***")
    print(pname," score is: ", pscore)
    print(opponent," score is: ", oscore)
    
    if pscore > oscore:
        victor = pname
    elif oscore > pscore:
        victor = opponent
    else:
        victor = "Tie!"
    print("Current Winner is: ",victor)
    
    #check for playing again
    again = input("Again? ")
    again = again.lower()
    proll = 0