"""Create List"""

dataList = []

infile = open("DataFile.txt", 'r')

for line in infile:
    dataList.append(line.strip())
infile.close()

print(dataList)
