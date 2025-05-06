import csv
import os
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)
for row in data:
    print(row)
f.close()
