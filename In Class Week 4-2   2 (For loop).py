# Display a cartoon character with a specified last name.
lastName = input("Enter a last name to find your cartoon character(s): ")
found = False
infile = open("DataFile.txt", 'r')

for line in infile:
    if line.startswith(lastName):
        print(line.rstrip())
        found = True
infile.close()
if not found:
    print("No cartoon character had the last name ", lastName + '.')
