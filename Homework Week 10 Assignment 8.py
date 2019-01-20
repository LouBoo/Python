"""
Author:  Louis Booth
Name:    Homework Week 10 Assignment 8.py
Purpose: To create list of lists from csv, populate dictionary from list of lists
         Calculate exchange of currency, and display new converted value
Date:    4/6/2018
"""

def main():
    """
    call on various functions, allow user to exit program
    """
    print("Welcome to the currency conversion program!")
    while True:
        print()
        run = input(
            "Enter \"yes\" or \"y\" to run the converter, " +
            "enter anything else to exit: ").lower()
        if run == "yes" or run == "y":
            rates = fileToList("Exchrate.txt")
            rates2 = listToDict(rates)
            choices(rates2)
            start, end, startValue = getInput(rates2)
            endValue = calcExchRate(rates2, start, end, startValue)
            displayOutput(rates2, start, end, startValue, endValue)
        else:
            break

def fileToList(fileName):
    """
    create list of lists from csv file
    """
    infile = open(fileName, 'r')
    listOfExchrate = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfExchrate)):
        listOfExchrate[i] = listOfExchrate[i].split(',')
        listOfExchrate[i][0] = listOfExchrate[i][0]
        listOfExchrate[i][1] = listOfExchrate[i][1]
        listOfExchrate[i][2] = eval(listOfExchrate[i][2])
    return listOfExchrate

def listToDict(listName):
    """
    populate dictionary using list of lists, tuple as values
    """
    ratesDict = {}
    for i in range(len(listName)):
        ratesDict[listName[i][0]] = (listName[i][1], float(listName[i][2]))
    return ratesDict

def choices(dictName):
    """
    display choices (keys) for user in rows of 7
    """
    print()
    keys = list(dictName.keys())
    j = int(len(keys)/7)
    for i in range(j):
        print(" | ".join(keys[i*7:(i+1)*7]))
    print()

def getInput(dictName):
    """
    get user input and validate
    """
    print("Enter country names exactly as they appear in the list above.\n")
    while True:
        countryStart = input(
            "Please enter a country whose currency you wish to convert from: ")
        if countryStart not in dictName.keys():
            print("Input Error! Country name must be as it appears above.")
        else:
            break
    while True:
        countryEnd = input(
            "Please enter a country whose currency you wish to convert to: ")
        if countryEnd not in dictName.keys():
            print("Input Error! Country name must be as it appears above.")
        else:
            break
    while True:
        try:
            startValue = float(input("Please enter a value to convert: "))
            break
        except ValueError:
            print("Input Error! Value must contain only digits and a decimal.")
    return countryStart, countryEnd, startValue

def calcExchRate(dictName, stringName1, stringName2, startValue):
    """
    calculate converted value by referencing dictionary based on user input
    """
    endValue = (startValue/
             dictName[stringName1][1])*dictName[stringName2][1]
    return endValue

def displayOutput(dictName, stringName1, stringName2, startValue, endValue):
    """
    display output with proper formatting
    """
    print()
    if startValue == 1 and endValue != 1:
        print("{0:,.2f} {1:} from {2:} converts to {3:,.2f} {4:}s in {5:}."
              .format(startValue, dictName[stringName1][0], stringName1,
                      endValue, dictName[stringName2][0], stringName2))
    elif startValue != 1 and endValue == 1:
        print("{0:,.2f} {1:}s from {2:} converts to {3:,.2f} {4:} in {5:}."
              .format(startValue, dictName[stringName1][0], stringName1,
                      endValue, dictName[stringName2][0], stringName2))
    elif startValue == 1 and endValue == 1:
        print("{0:,.2f} {1:} from {2:} converts to {3:,.2f} {4:} in {5:}."
              .format(startValue, dictName[stringName1][0], stringName1,
                      endValue, dictName[stringName2][0], stringName2))
    else:
        print("{0:,.2f} {1:}s from {2:} converts to {3:,.2f} {4:}s in {5:}."
              .format(startValue, dictName[stringName1][0], stringName1,
                      endValue, dictName[stringName2][0], stringName2))

main()
