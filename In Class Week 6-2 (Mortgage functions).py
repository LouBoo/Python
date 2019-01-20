def main():
    print("Calculate monthly mortgage payment!")
    print()
    P, r, n, n_yrs, r_annual = getInput()

    ## calling the mortgage function
    monthlyPlay = mnth_pay(P, r, n)

    ## calling the output function
    output_Data(P, r_annual, monthlyPay, n_yrs)

def getInput():
    P = float(input("Enter the principal of your mortgage: "))
    while not (P > 0):
        P = float(input("Enter the principal of your mortgage: "))
    r_annual = float(input("Enter the annual interest rate,  i.e., 4.25 for 4.25 percent: "))
    while not (100 > r_annual > 0):
        r_annual = float(input("Enter the annual interest rate, i.e., 4.25 for 4.25 percent: "))
    n_yrs = float(input("Enter the duration of your mortgage in years: "))
    while not (n_yrs > 0):
        n_yrs = float(input("Enter the duration of your mortgage in years: "))
    r = (r_annual / 12) / 100
    n = (n_yrs * 12)
    return P, r, n, n_yrs, r_annual

def mnth_pay(P, r, n):
    """
    Input:  P, the principal
            r, monthly interest rate
            n, duration of loan in months
    Returns monthly mortgage payment
    """
    M = P * ((r * (1 + r)**n) / ((1 + r)**n - 1))
    return M

def output_Data(P,r, pay, n):
    """
    Input:  P, the principal
            r, annual interest rate
            pay, the monthly payment after calculation
            n, duration of loan in years
    """
    print()
    print("With a principal of ${0:,.2f}; an annual interest rate of {1:g}%;".format(P, r)) 
    print("and a duration of {:g} years: Your monthly payment is about: ${:,.2f}".format(n, pay))

main()
