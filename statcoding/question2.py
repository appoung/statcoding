import csv
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
max_ilgyocha = -999
max_date = ''
for row in data:
    if row[4] == '':
        row[4] = previous_highest_temp
    if row[3] == '':
        row[3] = previous_lowest_temp

    row[4] = float(row[4])
    row[3] = float(row[3])
    ilgyocha = row[4] - row[3]
    if max_ilgyocha < ilgyocha:
        max_ilgyocha = ilgyocha
        max_date = row[0]
    previous_highest_temp = row[4]
    previous_lowest_temp = row[3]
print('max_ilgyocha:', max_ilgyocha)
print('max_date:', max_date)
f.close()
