import csv
max_temp = -999
max_date = ''
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
for row in data:

    if row[4] == '':
        row[4] = previous_highest_temp
    row[4] = float(row[4])
    if max_temp < row[4]:
        max_temp = row[4]
        max_date = row[0]
    previous_highest_temp = row[4]
print('max_temp:', max_temp)
print('max_date:', max_date)
f.close()
