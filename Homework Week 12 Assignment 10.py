"""
Author:  Louis Booth
Name:    Homework Week 12 Assignment 10.py
Purpose: create rock, paper, scissors program
Date:    4/17/2018
"""

import random

def main():
    selectMenu()    

def rockPaperScissors(string, listName):
    """
    takes user's choice, generates computer's choice and compares them
    return outcome
    """
    computerChoice = random.choice(listName)
    if string == "rock":
        if computerChoice == "rock":
            outcome = "draw"
        elif computerChoice == "paper":
            outcome = "loss"
        else:
            outcome = "win"
    elif string == "paper":
        if computerChoice == "rock":
            outcome = "win"
        elif computerChoice == "paper":
            outcome = "draw"
        else:
            outcome = "loss"
    else:
        if computerChoice == "rock":
            outcome = "loss"
        elif computerChoice == "paper":
            outcome = "win"
        else:
            outcome = "draw"
    return computerChoice, outcome

def selectMenu():
    """
    Display rules of game and choices for user
    Take user input, call on rockPaperScissors() function to determine outcome
    Display user's choice, computer's choice, and result with proper formatting
    Allow user to quit program
    """
    print("Welcome to the Rock, Paper, Scissors program!")
    print("\nThe rules are as follows:")
    print("Rock beats scissors; Paper beats rock; Rock and rock is a draw.")
    print("Paper beats rock; Scissors beats paper; Paper and paper is a draw.")
    print("Scissors beats paper; Rock beats scissors; Scissors and scissors is a draw.")
    print()
    listOfChoices = ["rock", "paper", "scissors"]
    while True:
        print("To choose rock, enter 1.")
        print("To choose paper, enter 2.")
        print("To choose scissors, enter 3.")
        print("To quit the program, enter 4.")
        print()
        try:
            c = int(input("Please enter a number between 1 and 4: "))
            if c == 1:
                choice = "rock"
                compHand, outcome = rockPaperScissors(choice, listOfChoices)
                print("\nYour choice was:", choice, "\nComputer's choice was:", compHand)
                print("\nThe game resulted in a {}.\n\n".format(outcome))
            elif c == 2:
                choice = "paper"
                compHand, outcome = rockPaperScissors(choice, listOfChoices)
                print("\nYour choice was:", choice, "\nComputer's choice was:", compHand)
                print("\nThe game resulted in a {}.\n\n".format(outcome))
            elif c == 3:
                choice = "scissors"
                compHand, outcome = rockPaperScissors(choice, listOfChoices)
                print("\nYour choice was:", choice, "\nComputer's choice was:", compHand)
                print("\nThe game resulted in a {}.\n\n".format(outcome))
            elif c == 4:
                print("\nThank you for playing! Goodbye!")
                break           
        except ValueError:
            print("Input Error! Value must be a number./n")     

main()
