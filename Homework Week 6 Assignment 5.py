def mnth_pay(P, r, n):
    """
    Input:  P, the principal
            r, monthly interest rate
            n, duration of loan in months
    Returns monthly mortgage payment
    """
    M = P * ((r * (1 + r)**n) / ((1 + r)**n - 1))
    return M

print("Calculate monthly mortgage payment!")

print()

while True:
    try:
        P = float(input("What is the principal of your mortgage?: "))
        if P > 0:
            r_annual = float(input("What is the annual interest rate on your mortgage?: "))
            if r_annual > 0 and r_annual < 100:
                n_yrs = float(input("What is the duration of your mortgage in years?: "))
                if n_yrs > 0:
                    r = (r_annual / 12) / 100
                    n = (n_yrs * 12)
                    print()
                    print("With a principal of ${:,.2f}; an annual interest rate of {:g}%;".format(P, r_annual)) 
                    print("and a duration of {:g} years: Your monthly payment is about: ${:,.2f}".format(n_yrs, mnth_pay(P, r, n)))
                    break
                else:
                    print("Input Error! Value must be positive.")
            else:
                print("Input Error! Value must a positive number between 0 and 100.")
        else:
            print("Input Error! Value must be positive.")
    except ValueError:
        print("Input Error! Values must be positive numbers.")

print()
print()

infile = open("planets.txt", 'r')
planet_list = []

for line in infile:
    if line.isalpha:
        planet_list.append(line.rstrip())

planet_list.sort()
planet_list = planet_list[:5]
print(planet_list)







