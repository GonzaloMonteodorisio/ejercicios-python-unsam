import sys
import csv
f = open('../Data/missing.csv', encoding='utf8')

rows = csv.reader(f)
# next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
headers = next(rows)
costo_total = 0

for i, row in enumerate(rows, start=1):
    try:
        costo_total += float(row[1]) * float(row[2])
        #print(costo_total)
    except ValueError:
        print(f'Fila {i}: No puede interpretar: {row}')
f.close()
print(f'Costo total: {costo_total}')