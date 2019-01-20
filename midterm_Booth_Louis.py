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
    numbers = range(0, 100, 2)
    numSum = sum(numbers)
    return numSum

def calcPay(x,y,z):
    cost = x * (1 + y + z)
    return cost

def selectMenu():
    print("To calculate a sum of odd integers between 1 and 99, enter 1.")
    print("To calculate the final payment for a meal consumed in a restaurant, enter 2.")
    print("To calculatea value \"x\" raised to the power of \"n\", enter 3.")
    print("To quit the program, enter 4.")
    print()
    while True:
        try:
            c = int(input("Please enter a number between 1 and 4: "))
            if c == 1:
                 numSum = calcSum()
                 print(numSum)
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
                              "Please enter the local tax rate as a decimal, e.g. .08 for 8%%: "))
                        if y > 0 and y < 1:
                            break
                     except ValueError:
                        print("Input Error! Value must be a positive decimal between 0 and 1.")
                while True:
                    try:
                        z = float(input(
                            "Please enter the local tipping rate as a decimal, e.g. .08 for 8%%: "))
                        if z > 0 and z < 1:
                            break
                    except ValueError:
                        print("Input Error! Value must be a positive decimal between 0 and 1.")
                pay = calcPay(x,y,z)
                print("${:,.2f}".format(pay))
            elif c == 3:
                 while True:
                    try:
                        x = int(input("Please enter an integer: "))
                        break
                    except ValueError:
                        break
                 while True:
                    try:
                        n = int(input("Please enter an integer power: "))
                        break
                    except ValueError:
                        break
                 power = findPower(x,n)
                 print(power)
            elif c == 4:
                break
            else:
                print("Input Error! Values must be between 1 and 4.")
        except ValueError:
            print("Input Error! Values must be between 1 and 4.")
    
    return c
        
main()  

