## Calculate an average grade. Drop two lowest grades.
import letter

grades = []
i = 0

while (i < 7):
    grade = int(input("Enter a grade between 0 and 100: "))
    if not (0 <= grade <= 100):
        grade = int(input("Enter a grade between 0 and 100: "))
        if (0 <= grade <= 100):
            grades.append(grade)
            i += 1
    else:
        grades.append(grade)
        i += 1

grades.sort()
grades = grades[1:] 
average = sum(grades) / len(grades)
print("Average grade: {0:.2f}%".format(average))
print('Your letter grade is: ', letter.letter_grade(average))
