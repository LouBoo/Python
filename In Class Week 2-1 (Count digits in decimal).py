while True:
    try:
        number = int(input("Enter positive number containing decimal: "))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        continue
    try:
        right = str(number)[::-1].find('.')
        if right >= 0:
            print ("%s digits to the right of decimal." % right)
        else:
            print ("0 digits to the right of decimal.")
        break
        continue
    try:
        left = str(number)[::1].find('.')
        if left >= 0:
            print ("%s digits to the left of decimal." % left)
        else:
            print ("0 digits to the left of decimal.")
        break
        continue

print ("%s digits to the left of decimal." % left)




print ("%s digits to the right of decimal." % right)

response = input("Enter a sentence: ")
response2 = input("Enter a word to be replaced: ")
response3 = input("Enter replacement word: ")
my_text = response
my_text = my_text.replace(response2, response3)
print (my_text)
