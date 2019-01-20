while True:     #To ensure input is positive non-zero number in decimal format
    try:
        number = float(input("Enter a positive number containing a decimal: "))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        continue

right = str(number)[::-1].find('.')
print("%d digits to the right of decimal." %right)

left = str(number)[::1].find('.')
print("%d digits to the left of decimal." %left)




response = input("Enter a sentence: ")
response2 = input("Enter a word to be replaced: ")
response3 = input("Enter replacement word: ")
my_text = response
my_text = my_text.replace(response2, response3)
print(my_text)
