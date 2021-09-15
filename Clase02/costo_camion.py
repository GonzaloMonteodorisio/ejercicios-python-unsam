import sys
import csv
f = open('../Data/missing.csv', encoding='utf8')

rows = csv.reader(f)
# next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
headers = next(rows)
costo_total = 0

for row in rows:
    try:
        costo_total += float(row[1]) * float(row[2])
        #print(costo_total)
    except ValueError:
        print(f'El número de cajones no puede ser un string vacío.','El tipo de error es: ', sys.exc_info()[0])
f.close()
print(f'Costo total: {costo_total}')