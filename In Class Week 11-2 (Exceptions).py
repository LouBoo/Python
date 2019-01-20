"""
Name:    In Class Week 11-2.py
Purpose: To practice implementing exceptions
Date:    4/12/2018
"""

"""general format ##############################################################
try:
    do your operations that you think might cause uncontrollable errors here
    ...
except:
    if there is any exception, then execute this block of code
    ...
else:
    if there is no exception then execute this block of code
################################################################################
"""

import pickle

def main():
    readFile()
    writeFile()
    getInput()
    

"""catch specified type of exception and use else clause
################################################################################
"""
def readFile():
    try:
        infile = open("aFile.dat", 'rb')
        ditnName = pickle.load(infile)
        infile.close()
    except (IOError, FileNotFoundError):
        print("Error: Cannot find or read data.")
    else:
        print("The file was opened successfully!")

"""catch unspecified type of exception and finally else clause
################################################################################
"""
def writeFile():
    try:
        outfile = open("bFile.dat", 'wb')
        pickle.dump(ditnName, outfile)
    except Exception as exp:
        print("Error: in writeFile()", exp)
    finally:
        outfile.close()

"""catch specified type of exception
################################################################################
"""
def getInput():
    ditnAlphabet = {'a':"alpha", 'b':"bravo", 'c':"charlie"}
    while True:
        try:
            letter = input("Enter a, b, or c: ")
            print(ditnAlphabet[letter])
            break
        except KeyError:
            print("Unacceptable letter was entered.")

main()
