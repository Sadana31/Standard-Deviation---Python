import math

import csv

with open("data.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def findMean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean

squaredList = []
for number in data:
    a = int(number) - findMean(data)
    a = a**2
    squaredList.append(a)

sum = 0
for i in squaredList:
    sum = sum + i

result = sum / (len(data)-1)

standard_deviation = math.sqrt(result)
print(standard_deviation)




