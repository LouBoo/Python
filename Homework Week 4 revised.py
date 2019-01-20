def index(string, chars):
    try:
        return min(string.index(vowels) for vowel in vowels if vowel in string)
    except ValueError:
        return -1
print("Welcome to the English to Pig Latin word translator!")
while True:
    english = str(input("Enter an English word with no punctuation, spaces, or numbers: "))
    english_lower = english.lower()
    if english.isalpha():
        vowels = "aeiou"      #Could add "y" to vowels
        if index(english_lower, vowels) == 0:
            pig_vow = "way"
            pig_latin = english_lower + pig_vow
        elif index(english_lower, vowels) > 0:
            pig_con = "ay"
            pig_latin = english_lower[index(english_lower, vowels):] + english_lower[0:index(english_lower, vowels)] + pig_con
        else:
            pig_con = "ay"
            pig_latin = english_lower + pig_con
        break
    else:
        print("Input error! Blank, numeric, or symbolic character(s) preventing conversion.") 
print("Conversion complete: " + english_lower + " becomes " + pig_latin + ".")

print()

print("Convert number grade to letter grade:")
while True:
    test = eval(input("Enter an average test score on a scale of 0 to 100: "))
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
