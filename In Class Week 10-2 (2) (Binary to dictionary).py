"""
Name:    In Class Week 10-2 (2).py
Purpose: To practice how to store a dictionary in binary format
Date:    4/5/2018
"""

import pickle

def main():
    presDict = createDictFromBinaryFile("USpresStatesDict.dat")
    state = getState(presDict)
    display = displayOutput(state, presDict)

# create a dictionary from the binary file
def createDictFromBinaryFile(fileName):
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()
    return dictionaryName

# get the state each president came from
def getState(dictionaryName):
    state = input("Enter the name of a state: ")
    if state in dictionaryName.values():
        return state
    else:
        return "There are no presidents from " + state + "."

# display the results to the user
def displayOutput(state, dictionaryName):
    if state.startswith("There"):
        print(state)
    else:
        print("Presidents from", state + ":")
        for pres in sorted(dictionaryName):
            if dictionaryName[pres] == state:
                print("    " + pres[1] + " " + pres[0])

main()
