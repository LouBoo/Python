"""
Name:    ReadFile.py
Purpose: To practice how to read a text file using a 'for' loop
Date:    2/7/2018
"""

# Display a cartoon character with a specified last name.
lastName = input("Enter a last name to find your cartoon character(s): ")
found = False
infile = open("DataFile2.txt", 'r')

for line in infile:
    if line.endswith(lastName + "\n"):
        print(line.rstrip())
        found = True
infile.close()
if not found:
    print("No cartoon character had the last name ", lastName + '.')
