"""
Author:  Louis Booth
Name:    Homework Week 7 Assignment 7.py
Purpose: To create list from csv, sort by population in 2015
         Calculate growth rate, and write new csv file
Date:    3/5/2018
"""

def main():
    """
    create list from CSV file, calculate growth rate between two years
    and extend list. Order list by population in 2015.  
    Display the five cities with the highest population in 2015.
    create a new CSV file containing list of cities ordered by growth rate.
    Display list contents in table.  Display contents of new CSV file.
    """
    cities = csvToList("US_Cities.txt")
    cities.sort(key=lambda City:City[3], reverse=True)
    displayTopFive(cities)
    cities.sort(key=lambda Growth:Growth[4], reverse=True)
    newCsvFile(cities)
    

def csvToList(fileName):
    """
    function name: csvToList
    purpose:       creates a list using the read-in information of a CSV file.
                   Calculates growth rate between two years and extends list. 
    parameters:    a file (CSV)
    return:        a list (each element is also a list)
    """
    infile = open(fileName, 'r')
    listOfCities = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(listOfCities)):
        listOfCities[i] = listOfCities[i].split(',')
        listOfCities[i][1] = listOfCities[i][1]
        listOfCities[i][2] = eval(listOfCities[i][2]) * 100000
        listOfCities[i][3] = eval(listOfCities[i][3]) * 100000
        growthRate = [((listOfCities[i][3] - listOfCities[i][2])
                              / listOfCities[i][2]) * 100]
        listOfCities[i].extend(growthRate)
    return listOfCities


def displayTopFive(listName):
    """
    function name: displayTopFive
    purpose:       display the five cities with the highest 2015 population
    parameters:    a list of cities
    return:        None
    """
    print()
    print("Five cities with the highest populations in 2015:")
    print()    
    print("{0:<8}|{1:^16}|{2:>15}".format("Rank", "City", "Pop. in 2015"))
    print("-----------------------------------------")
    for i in range(0, 5):
        print("{0:<8}|{1:^16}|{2:>15,.0f}"
              .format(i+1, listName[i][0], listName[i][3]))

def newCsvFile(listName):
    """
    function name: popGrowthFile
    purpose:       create a new file in CSV format from list
                   display contents of list in table
                   display contents of new file
    parameters:    a list of cities
    return:        None
    """
    print("\n")
    print("New file \"growth.txt\" will contain the following\n"
          + "\"City\" and \"Growth Rate\" information in CSV format:\n")
    print("{0:<6}|{1:^18}|{2:^8}|{3:^15}|{4:^15}|{5:>12}"
          .format("Rank", "City", "State", "Pop. in 2005", "Pop. in 2015", "Growth Rate"))
    print("-------------------------------------------------------------------------------")
    for i in range(len(listName)):
        print("{0:<6}|{1:^18}|{2:^8}|{3:^15,.0f}|{4:^15,.0f}|{5:11.2f}%"
              .format(i+1, listName[i][0], listName[i][1], listName[i][2], listName[i][3], listName[i][4]))
    print()
    print("Writing new file \"growth.txt\"...\n")
    outfile = open("growth.txt", 'w')
    for i in range(len(listName)):
        outfile.write(listName[i][0] + "," + "%.2f \n" %listName[i][4])
    outfile.close()
    print("File \"growth.txt\" contains:")
    print()
    infile = open("growth.txt", 'r')
    growthList = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(growthList)):
        print("{0:}".format(growthList[i]))
        
main()
