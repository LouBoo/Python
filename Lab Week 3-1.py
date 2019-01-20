def isFloat(string):
    if type(float(string)) == type(0.1):
        return 1
    else:
        return 0

a = input("Enter a float: ")
print(isFloat(a))
