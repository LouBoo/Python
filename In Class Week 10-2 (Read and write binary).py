"""
Name:    In Class Week 10-2.py
Purpose: To practice how to store a dictionary in binary format
Date:    4/5/2018
"""

import pickle

def main():
    writefile()
    readFile()

def writeFile():
    outfile = open(fileName, 'wb') # the file name could be "abc.dat"
    pickle.dump(dictionaryName, outfile)
    outfile.close()

def readFile():
    infile = open(fileName, 'rb')
    dictionaryName = pickle.load(infile)
    infile.close()

main()
