"""
Demonstrating some dictionary functions and operations
Create a frequency dictionary
3/29/2018
"""

def main():
    # declare an empty dictionary
    ditn = {}
    # add an item to the dictionary
    ditn["apple"] = 3
    # check your result
    print(ditn)
    # modify value of apple and add another item to dictionary
    ditn.update({"apple":1, "banana":2})
    # check your result
    print(ditn)
    # use len() of dictionary
    print("ditn has", len(ditn), "items")
    # check if banana is a key in the dictionary, will return True/False
    print("banana" in ditn)
    # add two more items to dictionary
    ditn["cherry"] = 3
    ditn["pear"] = 2
    # check your result
    print(ditn)
    # print a list of keys in the dictionary - use .key() & put into a list
    print("keys:", list(ditn.keys()))
    # print a list of values in the dictionary - use .values() & put into a list
    print("values:", list(ditn.values()))
    # use alternative way to display the entire dictionary
    for key in ditn:
        print(key, ditn[key])
    # check if an item is in the dictionary - use .get(key, default)
    # return the corresponding value if it exists and default if not
    print(ditn.get("orange", "Item is not in the dictionary"))
    print("The value for this item is:", ditn.get("cherry", "Item is not in the dictionary"))

    # create new dictionary
    ditn2 = {}
    # copy first dictionary into the second dictionary
    ditn2 = dict(ditn)
    # check your result
    print(ditn2)
    # delete items from second dictionary (ditn2), it will raise an exception
    # if not found
    del ditn2["banana"]
    # check if item was deleted
    print("ditn2 after deleting banana:", ditn2)
    # modify ditn2
    ditn2.update({"orange":5, "kiwi":4, "pear":7, "cherry":8})
    # check your results
    print("ditn2 after adding more items:", ditn2)
    # merge the two dictionaries
    ditn.update(ditn2)
    # check if merge was successful
    print("After merging the two dictionaries, ditn contains:", ditn)  # values in ditn2 replace values in ditn
    
main()
