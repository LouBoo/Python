"""
Author:  Louis Booth
Name:    midterm_Booth_Louis.py
Purpose: menu selection of various functions
Date:    3/22/2018
"""

def main():
    selectMenu()    

def findPower(x, n):
    x_n = x**n
    return x_n

def calcSum():
    numbers = range(1, 100, 2)
    numSum = sum(numbers)
    return numSum

def calcPay(x,y,z):
    cost = x * (1 + y + z)
    return cost

def selectMenu():
    print("To calculate a sum of odd integers between 1 and 99, enter 1.")
    print("To calculate the final payment for a meal consumed in a restaurant, enter 2.")
    print("To calculate a value \"x\" raised to the power of \"n\", enter 3.")
    print("To quit the program, enter 4.")
    print()
    while True:
        try:
            c = int(input("Please enter a number between 1 and 4: "))
            if c == 1:
                 print("The sum of all odd integers between, and including, 1 to 99 is: {:}.".format(calcSum()))
                 print()
            elif c == 2:
                while True:
                    try:
                         x = float(input("Please enter the cost of food: "))
                         break
                    except ValueError:
                         print("Input Error! Value must be a positive integer or float.")
                while True:
                     try:
                        y = float(input(
                              "Please enter the local tax rate as a decimal, e.g. .08 for 8%: "))
                        if y > 0 and y < 1:
                            break
                     except ValueError:
                        print("Input Error! Value must be a positive decimal between 0 and 1.")
                while True:
                    try:
                        z = float(input(
                            "Please enter the local tipping rate as a decimal, e.g. .08 for 8%: "))
                        if z > 0 and z < 1:
                            break
                    except ValueError:
                        print("Input Error! Value must be a positive decimal between 0 and 1.")
                print("Final payment amount is: ${:,.2f}".format(calcPay(x,y,z)))
                print()
            elif c == 3:
                while True:
                    try:
                        x = int(input("Please enter an integer: "))
                        break
                    except ValueError:
                        print("Input Error! Value must be an integer.")
                while True:
                    try:
                        n = int(input("Please enter an integer power: "))
                        break
                    except ValueError:
                        print("Input Error! Value must be an integer.")
                print("{0:,} raised to the power of {1:,} is: {2:,}".format(x, n, findPower(x,n)))
                print()
            elif c == 4:
                break
            else:
                print("Input Error! Value must be between 1 and 4.")
        except ValueError:
            print("Input Error! Value must be between a number between 1 and 4.")

main()  

