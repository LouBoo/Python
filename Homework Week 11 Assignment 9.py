"""
Name:    Homework Week 11 Assignment 9.py
Purpose: To practice how to use a tuple for key in a dictionary
         To practice implementing exceptions
Date:    4/10/2018
"""

import pickle

def main():
    presDict = createDictFromBinaryFile("USpresStatesDict.dat")
    state = getState(presDict)
    displayOutput(state, presDict)
   
def createDictFromBinaryFile(fileName):
    try:
        infile = open(fileName, 'rb')
    except FileNotFoundError:
        print("File \"{}\" not found.".format(fileName))
    else:
        dictionaryName = pickle.load(infile)    
        infile.close()
        return dictionaryName

def getState(dictName):
    state = input("Enter the name of a state: ")
    try:
        if state in dictName.values():
            return state
        else:
            return "There are no presidents from " + state + '.'
    except AttributeError:
        print("Dictionary not found.")

            

def displayOutput(state, dictName):
    try:
        if state.startswith("There"):
            print(state)
        else:
            print("Presidents from", state + ':')
            for pres in sorted(dictName):
                if dictName[pres] == state:
                    print("  " + pres[1] + " " + pres[0])
    except AttributeError:
        print("Nothing to display")

main()




    
