def main():
    """
    create a file containing good performers in DOW stocks
    ordered by company's name. Display the first thre lines of the file.
    """
    firms = putRecordIntoList("DOW_Stocks.txt")
    firms.sort(key=lambda firm:firm[:][0])  # sort by firm name
    displayFirstThree(firms)
    createNewFile(firms)    # create new CSV file with new order

def putRecordIntoList(fileName):
    """
    function name:  putRecordIntoList
    purpose:        creates a list using the read-in information of a csv file
    parameters:     a file (CSV)
    return:         a list (each element is also a list)
    """
    infile = open(fileName, 'r')
    listOfRecords = [line.rstrip() for line in infile]
    infile.close()
    # loop through each element of the list and parse each record
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')  # parsing each item of a record
    return listOfRecords

def displayFirstThree(listName):
    """
    function name:  displayFirstThree
    purpose:        display the first three firms in alphabetical order
    parameters:     a list of firms
    return:         None
    """
    print("{0:18}{1:10}{2:10}".format("Firm", "Symbol", "Yield"))
    for i in range(3):
        print("{0:18}{1:10}{2:10}".format(listName[i][0], listName[i][1], listName[i][2]))

def createNewFile(listName):
    """
    function name:  createNewFile
    purpose:        creates a new file in CSV format with one less item
    parameters:     a list of firms
    return:         None
    """
    outfile = open("FirmsByName.txt", 'w')
    for element in listName:
        outfile.write(element[0] + ',' + element[2] + "\n")

# invoke main
main()
        
