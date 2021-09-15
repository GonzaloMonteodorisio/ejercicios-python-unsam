import csv
f = open('../Data/camion.csv', encoding='utf8')
rows = csv.reader(f)
print(rows)
headers = next(rows)
print(headers)
for row in rows:
    print(row)
f.close()