while True:
    try:
        test1 = int(input("Please enter a test score between 0 and 100: "))
        if test1 < 0 or test1 > 100:
            raise ValueError
        break
    except ValueError:
        print("Please enter a number between 0 and 100.")
        
