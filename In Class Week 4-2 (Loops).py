# using for loop
mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(7, 10):
    mysum += i
    print(mysum)


"""
Loop practice in class
Find how you can correct the following programs """

init_val = 10
while init_val > 0:

    print(init_val)
    init_val -= 1       #same as (init_val = init_val -1)
    #decrement init_val so it will go down and meet 5
    if init_val == 5:
        break
print(init_val)



# modify this one to allow the loop to execute atleast once

pswd = ""
while pswd.upper() != "PYTHON":
    pswd = input("Enter the password: ")
print("You can continue now.")



#modify this one so the letters list can be displayed as a string

letters = ['P', 'y', 't', 'h', 'o', 'n']
language = ""
i = 0
while letters: #This is the same as writing (while letters != []:)
    language += letters[i]
    #i = i + 1
    letters = letters[i+1:]
print(language)
