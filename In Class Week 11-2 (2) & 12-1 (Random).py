"""
Random Module
4/12/2018
"""

import random
import pickle

def main():
    basicSelection()
    print("")
    print("***********************Results of Playing Slot Machine**************************")
    slotMachine()
    print("\n")
    # get the deck of cards and then play poker
    listOfCards = getDeckOfCards()
    print("******************************Results of Poker**********************************")
    pokerHand1 = playPoker(listOfCards)
    pokerHand2 = playPoker(listOfCards)
    # print both hands
    print("Player 1's hand:", pokerHand1)
    print("Player 2's hand:", pokerHand2)


def basicSelection():
    # create a list
    listElements = ["gold", "wood", "water", "fire", "earth"]
    print(random.choice(listElements))
    print("using choice()", random.choice(listElements))
    print("using sample()", random.sample(listElements, 2))
    print("using shuffle()")
    random.shuffle(listElements)
    print(listElements)
    # using randint
    print("using randint()", random.randint(1, 6))

# play slot machine
def spinReels():
    n = random.randint(1, 20)
    if n > 15:
        return "Cherries"
    elif n > 10:
        return "Orange"
    elif n > 5:
        return "Plum"
    elif n > 2:
        return "Melon"
    elif n > 1 :
        return "Bell"
    else:
        return "Bar"

def slotMachine():
    for i in range(3):
        outcome = spinReels()
        print(outcome, end="  ")

# Let's play poker
def getDeckOfCards():
    infile = open("DeckOfCardsList.dat", 'rb')
    listOfCards = pickle.load(infile)
    infile.close()
    return listOfCards

def playPoker(fileName):
    return random.sample(fileName, 5)
    

main()
    
