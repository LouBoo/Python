#########Final
print("Find the roots of quadratic equations!")

while True:
    a = int(input("Please enter a nonzero number for a: "))
    if a != 0:
        break
    else:
        print("Input Error! Value must be nonzero number.")
        
b = int(input("Please enter a number for b: "))
c = int(input("Please enter a number for c: "))
import math
det = (b**2 - (4*a*c))

if det < 0:
    print("No real roots found.")
elif det == 0:
    x1 = ((-b - (math.sqrt(det)))/(2*a))
    x2 = ((-b + (math.sqrt(det)))/(2*a))
    print("One real root found. The root is: %.2f" %x1)
else:
    x1 = ((-b - (math.sqrt(det)))/(2*a))
    x2 = ((-b + (math.sqrt(det)))/(2*a))
    print("Two real roots found. The roots are: {:.2f} & {:.2f}".format(x1, x2))


print()

#####Final
print("Calculate average test score with average letter grade!")

score_list = []
i = 0

while i < 7:
    try:
        score = float(input("Please enter a test score between 0 and 100: "))
        if score >= 0 and score <= 100:
            score_list.append(score)
            i = i + 1
        else:
            print("Input Error! Please enter a nonnegative number between 0 and 100.")
    except ValueError:
        print("Input Error! Please enter a number between 0 and 100.")

score_list.sort()
score_list = score_list[1:]
avg_score = (sum(score_list) / len(score_list))

if avg_score >= 0 and avg_score < 60:
    print("%.2f%% is an F" %avg_score)
elif avg_score >= 60 and avg_score < 70:
    print("%.2f%% is a D" %avg_score)
elif avg_score >= 70 and avg_score < 80:
    print("%.2f%% is a C" %avg_score)
elif avg_score >= 80 and avg_score < 90:
    print("%.2f%% is a B" %avg_score)
else:
    print("%.2f%% is an A" %avg_score)



######Second Attempt
##score_list = []
##i = 0
##
##while i < 7:
##    score = str(input("Please enter a test score between 0 and 100: "))
##    score_list += score.split()
##    i = i + 1
##
##for i in range(len(score_list)):
##    score_list[i] = eval(score_list[i])
##
##score_list.sort()
##score_list = score_list[1:]
##avg_score = (sum(score_list) / len(score_list))
##
##if avg_score >= 0 and avg_score < 60:
##    print("%.2f%% is an F" %avg_score)
##elif avg_score >= 60 and avg_score < 70:
##    print("%.2f%% is a D" %avg_score)
##elif avg_score >= 70 and avg_score < 80:
##    print("%.2f%% is a C" %avg_score)
##elif avg_score >= 80 and avg_score < 90:
##    print("%.2f%% is a B" %avg_score)
##else:
##    print("%.2f%% is an A" %avg_score)
##
##
##
##    
##
########First Attempt
##print("Calculate average test score with average letter grade!")
##
##while True:
##    try:
##        test1 = eval(input("Please enter a test score between 0 and 100: "))
##        if test1 < 0 or test1 > 100:
##            raise ValueError
##        break
##    except ValueError:
##        print("Please enter a number between 0 and 100.")
##        
##while True:
##    try:
##        test2 = eval(input("Please enter a second test score between 0 and 100: "))
##        if test2 < 0 or test2 > 100:
##            raise ValueError
##        break
##    except ValueError:
##        print("Please enter a number between 0 and 100.")
##        
##while True:
##    try:
##        test3 = eval(input("Please enter a third test score between 0 and 100: "))
##        if test3 < 0 or test3 > 100:
##            raise ValueError
##        break
##    except ValueError:
##        print("Please enter a number between 0 and 100.")
##        
##while True:
##    try:
##        test4 = eval(input("Please enter a fourth test score between 0 and 100: "))
##        if test4 < 0 or test4 > 100:
##            raise ValueError
##        break
##    except ValueError:
##        print("Please enter a number between 0 and 100.")
##        
##while True:
##    try:
##        test5 = eval(input("Please enter a fifth test score between 0 and 100: "))
##        if test5 < 0 or test5 > 100:
##            raise ValueError
##        break
##    except ValueError:
##        print("Please enter a number between 0 and 100.")
##        
##while True:
##    try:
##        test6 = eval(input("Please enter a sixth test score between 0 and 100: "))
##        if test6 < 0 or test6 > 100:
##            raise ValueError
##        break
##    except ValueError:
##        print("Please enter a number between 0 and 100.")
##        
##while True:
##    try:
##        test7 = eval(input("Please enter a seventh test score between 0 and 100: "))
##        if test7 < 0 or test7 > 100:
##            raise ValueError
##        break
##    except ValueError:
##        print("Please enter a number between 0 and 100.")
##        
##test_min = min(test1, test2, test3, test4, test5, test6, test7)
##total = (test1 + test2 + test3 + test4 + test5 + test6 + test7 - test_min)
##avg_score = (total/6)
##
##if avg_score >= 0 and avg_score < 60:
##    print("%.2f%% is an F" %avg_score)
##elif avg_score >= 60 and avg_score < 70:
##    print("%.2f%% is a D" %avg_score)
##elif avg_score >= 70 and avg_score < 80:
##    print("%.2f%% is a C" %avg_score)
##elif avg_score >= 80 and avg_score < 90:
##    print("%.2f%% is a B" %avg_score)
##else:
##    print("%.2f%% is an A" %avg_score)
##
