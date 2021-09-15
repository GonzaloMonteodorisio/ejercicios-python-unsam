import sys
import csv
# leer camion
def leer_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding='utf8')

    rows = csv.reader(f)
    # next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
    headers = next(rows)
    camion = []
    for n_row, row in enumerate(rows):
        record = dict(zip(headers, row))
        camion.append(record)
    f.close()
    return camion

lista_camion = leer_camion('../Data/camion.csv')
# print(f'Lista camión: {lista_camion}')
# leer precios
def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'r', encoding='utf8')
    rows = csv.reader(f)
    precios = {}
    for row in rows:
        try:
            precios[row[0]] = row[1]
        except IndexError:
            pass
            # print('No se pueden leer los valores de una fila vacía')
    f.close()
    return precios

misPrecios = leer_precios('../Data/precios.csv')
# print(f'Dict_precios: {misPrecios}')
venta_total = 0.0
for producto in lista_camion:
    venta_total += float(misPrecios[producto['nombre']]) * int(producto['cajones'])

# print(f'La venta total fue de: {venta_total:0.2f}')

costo_camion = 0.0
for producto in lista_camion:
    costo_camion += int(producto['cajones']) * float(producto['precio'])

# print(f'El costo total del camión fue de: {costo_camion:0.2f}')
ganancia = venta_total - costo_camion
# if (venta_total > costo_camion):    
#     print(f'La ganancia fue de: {ganancia:0.2f}')
# elif (venta_total == costo_camion):
#     print('No hubo ganancias ni pérdidas, salimos derechos')
# else:
#     perdida = -(venta_total - costo_camion)
#     print(f'La pérdida fue de: {perdida:0.2f}')
# print(f'Ganancia: {ganancia:0.2f}')
######################################################
def hacer_informe(lista_cajones, dict_precios):
    lista_tuplas = []
    for line in lista_cajones:
        tupla = (line['nombre'], line['cajones'], float(line['precio']), round((float(dict_precios[line['nombre']]) - float(line['precio'])), 2))
        # print(f'Tupla: {tupla}')
        lista_tuplas.append(tupla)
    # print(f'Lista de tuplas: {lista_tuplas}')
    return lista_tuplas
lista_informe = hacer_informe(lista_camion, misPrecios)

def extraer_headers(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    f.close()
    return headers
headers = extraer_headers('../Data/camion.csv')
headers.append('cambio')
# print(f'Headers: {headers}')
        
#########################################################

for linea in lista_informe:
    print('%10s %10s %10.2f %10.2f' % linea)