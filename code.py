import csv
import math

with open('data.csv', newline='') as f:
    reader =csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    n = len(data)
    
    sum =0
    for x in data:
        sum = sum+int(x)
    
    mean = sum/ n

    return mean

squares = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squares.append(a)

total=0
for x in squares:
    total = total+int(x)


result = total/(len(squares)-1)

stddev = math.sqrt(result)

print(stddev)

