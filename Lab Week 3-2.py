pig_con = "ay"
pig_vow = "way"
def index(english_lower, chars):
    try:
        return min(english_lower.index(vowels) for vowels in chars if vowels in english_lower)
    except ValueError:
        return -1 
while True:
    english = str(input("Enter a word with no punctuation, spaces, or numbers: "))
    english_lower = english.lower()
    vowels = ("a", "e", "i", "o", "u")      #Could add "y" to vowels
    first = english_lower[0]
    if len(english) > 0 and english.isalpha():
        if first in (vowels[0:]):
            pig_latin = english + pig_vow
            print(pig_latin)
            break
        elif first not in (vowels[0:]) and index(english_lower, vowels) >= 0:
            pig_latin = english[index(english_lower, vowels):] + english[0:index(english_lower, vowels)] + pig_con
            print(pig_latin)
            break
        elif index(english_lower, vowels) < 0:
            pig_latin = english_lower + pig_con
            print(pig_latin)
            break
        else:
            continue
    else:
        print("Blank, numeric, or symbolic character(s) preventing conversion") 



while True:
    test = float(input("Enter an average test score on a scale of 0 to 100: "))
    if test >= 0 and test < 60:
        print("F")
        break
    elif test >= 60 and test < 70:
        print("D")
        break
    elif test >= 70 and test < 80:
        print("C")
        break
    elif test >= 80 and test < 90:
        print("B")
        break
    elif test >= 90 and test <= 100:
        print("A")
        break
    else:
        print("Please enter a number between 0 and 100")
