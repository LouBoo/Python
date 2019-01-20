def main():
    print("Calculate the factorial of a positive integer!")
    print()
    n = getN()
    fact(n)
    print()
    

def getN():
    """
    Returns n, a positive integer
    """
    while True:
        try:
            n = int(input("Please enter a positive integer: "))
            if n > 0:
                break
        except ValueError:
            print("Input Error! Value must be a positive integer.")
    return n

def fact(n):
    """
    Input:  n, positive integer
    Returns n_fact, factorial of n
    """
    import math
    n_fact = math.factorial(n)
    print("The factorial is: {:,}".format(n_fact))
    return n_fact

main()

print()

def main():
    print("Calculate next year's salary!")
    print()
    first_name, last_name, annual_pay = getInput()
    new_pay = salary(annual_pay)
    output_Data(first_name, last_name, new_pay)
    

def getInput():
    """
    Returns first_name, employee's first name
            last_name, employee's last name
            annual_pay, employee's annual salary
    """
    while True:
        first_name = str(input("Please enter your first name: "))
        if first_name.isalpha():
            break
    while True:
        last_name = str(input("Please enter your last name: "))
        if last_name.isalpha():
            break
    while True:
        try:
            annual_pay = float(input("Please enter your annual salary: "))
            if annual_pay > 0:
                break
        except ValueError:
            print("Input Error! Salary must be a positive number.")
    return first_name, last_name, annual_pay

def salary(annual_pay):
    """
    Input:  annual_pay, employee's annual salary
    Returns new_pay, employee's annual salary adjusted for raise
    """
    if annual_pay < 40000:
        new_pay = annual_pay * 1.05
    else:
        above_forty = annual_pay - 40000
        two_pct = above_forty * 1.02
        new_pay = 40000 + two_pct + 2000
    return new_pay

def output_Data(first_name, last_name, new_pay):
    """
    Input:  first_name, employee's first name
            last_name, employee's last name
            new_pay, employee's annual salary adjusted for raise
    """
    print()
    print("{} {}, your salary next year will be: ${:,.2f}"
          .format(first_name, last_name, new_pay))

main()


        
