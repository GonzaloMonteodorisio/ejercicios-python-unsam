import sys
import csv
from pprint import pprint
def leer_camion(nombre_archivo):
    f = open(nombre_archivo, encoding='utf8')

    rows = csv.reader(f)
    # next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
    headers = next(rows)
    costo_total = 0
    camion = []
    for row in rows:
        try:
            lote = {'nombre': row[0], 'cajones': int(row[1]), 'precio': float(row[2])}
            print(lote)
            camion.append(lote)
        except ValueError:
            print(f'El número de cajones no puede ser un string vacío', sys.exc_info()[0])
    pprint(camion)
    f.close()
    total = 0.0
    for cajon in camion:
        total += cajon['cajones'] * cajon['precio']
    print(f'Costo total: {total}')
leer_camion('../Data/camion.csv')