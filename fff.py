while True:
    try:
        number = float(input("Enter a positive number containing a decimal: "))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        continue

right = str(number)[::-1].find('.')
if right <= 0:
    print ("0 digits to the right of decimal.")
else:
    print ("%d digits to the right of decimal." % right)

left = str(number)[::1].find('.')
if left >= 0:
    print ("%d digits to the left of decimal." % left)
else:
    print ("0 digits to the left of decimal.")


