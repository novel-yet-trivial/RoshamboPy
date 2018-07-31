#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:02:30 2018

@author: AdamF
"""

#rock paper scissors
import random
import time

OPTIONS = {
1: '''\
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
2: '''\
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
3: '''\
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}
CODES = {
    1:"Rock",
    2:"Paper",
    3:"Scissors"}

reverse = str.maketrans('()', ')(')
def print_graphic(player, opponent):
    for p, o in zip(OPTIONS[player].splitlines(), OPTIONS[opponent].splitlines()):
        o = o.translate(reverse)[::-1] # mirror the opponent's hand
        print("{:<22}{}{:>22}".format(p, ' '*10, o))

ENEMIES = ["Randy","Kyle","Fred","Bill","Anthony","Johnny Fingers","Hypno Toad","Samantha","Lisa","Petunia","Amelia","Jessica","Sarah 'Brains' Stompanato"]

def choose_opponent(pname):
    while True:
        opponent = (random.choice(ENEMIES))
        if opponent != pname: #don't let computer name be the same as player's name
            return opponent

def one_game():
    proll = 0
    while proll > 3 or proll < 1:
        proll = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors.  Make your choice!  "))
    oroll = random.randint(1,3)
    print("Your roll: {} ({})".format(proll, CODES[proll]))
    print("Opponent roll: {} ({})".format(oroll, CODES[oroll]))

    #graphics time!
    print_graphic(proll, oroll)
    return proll, oroll

def main():
    again = "y"
    victor = "None"
    pscore = 0
    oscore = 0
    holdtime = random.randint(1,3)

    print("Rock, Paper, Scissors! (v1)")
    print("**********************")
    pname = input("Enter your name! ")
    pname = pname.capitalize()
    opponent = choose_opponent(pname)

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
        #play one game
        proll, oroll = one_game()

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
        again = input("Again? ").lower()

if __name__ == '__main__':
    main()
