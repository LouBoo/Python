"""
File Name:  In Class Week 10-1.py
Purpose:    Create a frequency dictionary mapping str:int
Date:       4/3/2018
Author:     Louis Booth
"""

def main():
    ## analyze word frequencies in the text file
    listOfWords = formListOfWords("Gettysburg.txt")
    freqDict = createFreqDictionary(listOfWords)
    displayWordCount(listOfWords, freqDict)
    displayMostCommonWords(freqDict)

def formListOfWords(fileName):
    infile = open(fileName, 'r')
    ## there aren't new line characters to get rid of
    originalLine = infile.readline().lower()
    ## remove punctuation marks from the line
    line = ""
    ## loop through original line to put each individual word into a list
    for char in originalLine:
        if ('a' <= char <= 'z') or (char == " "):
            line += char
            ## done with if statement and the for loop
    ## put each word into a list and return it
    listOfWords = line.split(' ')
    infile.close()
    return listOfWords

## create a frequency dictionary with each item having the form word:word frequency
def createFreqDictionary(aWordList):
    ## declare a dictionary
    freqDict = {}
    for word in aWordList:
        freqDict[word] = 0 ## initialize the word frequency dictionary
        ## done with this for loop
    for word in aWordList:
        ## add frequency to words
        freqDict[word] += 1
        ## done with this for loop
    return freqDict

def displayWordCount(aWordList, aDict):
    print("The file contains", len(aWordList), "words.")
    print("The file contains", len(aDict), "different words.")

def displayMostCommonWords(aDict):
    print("The most common words and their frequency are:")
    listOfMostCommonWords = []
    for word in aDict.keys():
        if aDict[word] >= 7:
            listOfMostCommonWords.append((word, aDict[word]))
            ## done with if statement and for loop
    listOfMostCommonWords.sort(key=lambda x:x[1], reverse=True)
    for item in listOfMostCommonWords:
        print("    ", item[0] + ":", item[1])
        ## done with this for loop
    
main()
