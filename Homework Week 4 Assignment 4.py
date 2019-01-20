print("Find the roots of quadratic equations!")

while True:
    try:
        a = float(input("Please enter a nonzero value for the quadratic coefficient (a): "))
        if a != 0:
            b = float(input("Please enter a value for the linear coefficient (b): "))
            c = float(input("Please enter a value for the constant (c): "))
            import math
            dis = (b**2 - (4*a*c))
            print()
            if dis < 0:
                print("No real roots found.")
            elif dis == 0:
                x1 = ((-b - (math.sqrt(dis)))/(2*a))
                x2 = ((-b + (math.sqrt(dis)))/(2*a))
                print("One real root found. The root is: %.2f" %x1)
            else:
                x1 = ((-b - (math.sqrt(dis)))/(2*a))
                x2 = ((-b + (math.sqrt(dis)))/(2*a))
                print("Two real roots found. The roots are: {:.2f} & {:.2f}".format(x1, x2))
            break
        else:
            print("Input Error! Value must be a nonzero number.")
    except ValueError:
        print("Input Error! Values must be numbers.")



print()
print()



print("Calculate the average of seven test scores with letter grade!")
score_list = []
i = 0

while i < 7:
    try:
        score = float(input("Please enter a test score between 0 and 100: "))
        if score >= 0 and score <= 100:
            score_list.append(score)
            i += 1
        else:
            print("Input Error! Please enter a nonnegative number between 0 and 100.")
    except ValueError:
        print("Input Error! Please enter a number between 0 and 100.")

score_list.sort()
score_list = score_list[1:]
avg_score = (sum(score_list) / len(score_list))
print()
print("After dropping the lowest test score:")

if avg_score >= 90:
    print("Your average score of %.2f%% is an A." %avg_score)
elif avg_score >= 80:
    print("Your average score of %.2f%% is a B." %avg_score)
elif avg_score >= 70:
    print("Your average score of %.2f%% is a C." %avg_score)
elif avg_score >= 60:
    print("Your average score of %.2f%% is a D." %avg_score)
else:
    print("Your average score of %.2f%% is an F." %avg_score)
