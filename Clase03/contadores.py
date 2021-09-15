import sys
import csv
from collections import Counter
# leer camion
def leer_camion(nombre_archivo):
    f = open(nombre_archivo, encoding='utf8')

    rows = csv.reader(f)
    # next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
    headers = next(rows)
    camion = []
    for n_row, row in enumerate(rows):
        record = dict(zip(headers, row))
        try:
            lote = (record['nombre'], int(record['cajones']), float(record['precio']))
            camion.append(lote)
        except ValueError:
            print(f'Fila {n_row}: no puede interpretar {row}', sys.exc_info()[0])
    f.close()
    return camion

lista_camion = leer_camion('../Data/fecha_camion.csv')
# print('la lista de mi camión es:', lista_camion)

# leer precios
def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'r', encoding='utf8')
    rows = csv.reader(f)
    precios = {}
    for row in rows:
        try:
            precios[row[0]] = row[1]
        except IndexError:
            print('No se pueden leer los valores de una fila vacía')
    f.close()
    return precios

misPrecios = leer_precios('../Data/precios.csv')
print('Mis precios son:', misPrecios)

venta_total = 0.0
for producto in lista_camion:
    venta_total += float(misPrecios[producto[0]]) * int(producto[1])

print(f'La venta total fue de: {venta_total:0.2f}')

costo_camion = 0.0
for producto in lista_camion:
    costo_camion += int(producto[1]) * float(producto[2])

print(f'El costo total del camión fue de: {costo_camion:0.2f}')

if (venta_total > costo_camion):
    ganancia = venta_total - costo_camion
    print(f'La ganancia fue de: {ganancia:0.2f}')
elif (venta_total == costo_camion):
    print('No hubo ganancias ni pérdidas, salimos derechos')
else:
    perdida = -(venta_total - costo_camion)
    print(f'La pérdida fue de: {perdida:0.2f}')

camion = leer_camion('../Data/camion.csv')
print(camion)
###################################################

total_cajones = Counter()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones

print(total_cajones['Naranja']) 

