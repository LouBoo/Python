"""
A mini English-Chinese dictionary function that translates English words to
Chinese words.
"""
def translateWord(color):
    if color == "red":
        return "hong"
    elif color == "blue":
        return "lang"
    elif color == "green":
        return "luee"
    elif color == "white":
        return "bai"

"""
This function is actually MAPPING English words (keys) to Chinese words
(values) and can be extended to include more words that associate a value
with each key.Some programming languages use this concept and provide more
efficient and felxible way to manage such data -- dictionary.
"""

## Above function can be written as:

translate = {"red":"hong", "blue":"lang", "green":"luee", "white":"bai"}

## the value of translate("red") is "hong", the value of "green" is "luee"


"""
keys --
* must be unique
* immutable type (int, float, string, tuple, bool)
* careful with float type as key

values --
* any type (immutable and mutable)
* can be duplicates
* dictionary values can be lists, even other dictionaries!

orderless - no particular order
"""

print(translate["white"])
print(translateWord("blue"))
