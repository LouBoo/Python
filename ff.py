while True:
    try:
        response = int(input("Enter positive number containing decimal: "))
        if response <= 0:
            raise ValueError
        break
    

a = str(response)[::-1].find('.')
if a > 0:
    response = int(input("Enter positive number containing decimal: "))
   
