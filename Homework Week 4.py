pig_con = "ay"
pig_vow = "way"
def index(string, chars):
    try:
        return min(string.index(chars) for chars in chars if chars in string)
    except ValueError:
        return -1
print("Welcome to the English to Pig Latin word translator.")
while True:
    english = str(input("Enter an English word with no punctuation, spaces, or numbers: "))
    english_lower = english.lower()
    if len(english) > 0 and english.isalpha():
        vowels = ("a", "e", "i", "o", "u")      #Could add "y" to vowels
        first = english_lower[0]
        if first in (vowels[0:]) and index(english_lower, vowels) == 0:
            pig_latin = english_lower + pig_vow
            print(pig_latin)
            break
        elif first not in (vowels[0:]) and index(english_lower, vowels) > 0:
            pig_latin = english_lower[index(english_lower, vowels):] + english_lower[0:index(english_lower, vowels)] + pig_con
            print(pig_latin)
            break
        elif index(english_lower, vowels) < 0:
            pig_latin = english_lower + pig_con
            print(pig_latin)
            break
        else:
            continue
    else:
        print("Input error! Blank, numeric, or symbolic character(s) preventing conversion.") 


print()


print("Convert number grade to letter grade.")
while True:
    test = float(input("Enter an average test score on a scale of 0 to 100: "))
    if test >= 0 and test < 60:
        print("%.2f%% is an F" %test)
        break
    elif test >= 60 and test < 70:
        print("%.2f%% is a D" %test)
        break
    elif test >= 70 and test < 80:
        print("%.2f%% is a C" %test)
        break
    elif test >= 80 and test < 90:
        print("%.2f%% is a B" %test)
        break
    elif test >= 90 and test <= 100:
        print("%.2f%% is an A" %test)
        break
    else:
        print("Input error! Please enter a number between 0 and 100.")
