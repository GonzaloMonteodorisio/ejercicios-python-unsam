import csv
# leer camion
def leer_camion(nombre_archivo):
    f = open(nombre_archivo, encoding='utf8')

    rows = csv.reader(f)
    # next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
    headers = next(rows)
    camion = []
    for n_row, row in enumerate(rows):
        record = dict(zip(headers, row))
        camion.append(record)
    f.close()
    return camion

lista_camion = leer_camion('C:/Users/Monty/Desktop/Chalo/ECyT - IAI - UNSAM/curso-python/ejercicios_python/Data/fecha_camion.csv')
print(lista_camion)
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

misPrecios = leer_precios('C:/Users/Monty/Desktop/Chalo/ECyT - IAI - UNSAM/curso-python/ejercicios_python/Data/precios.csv')
print(f'Precios: {misPrecios}')
venta_total = 0.0
for producto in lista_camion:
    venta_total += float(misPrecios[producto['nombre']]) * int(producto['cajones'])

print(f'La venta total fue de: {venta_total:0.2f}')

costo_camion = 0.0
for producto in lista_camion:
    costo_camion += int(producto['cajones']) * float(producto['precio'])

print(f'El costo total del camión fue de: {costo_camion:0.2f}')

if (venta_total > costo_camion):
    ganancia = venta_total - costo_camion
    print(f'La ganancia fue de: {ganancia:0.2f}')
elif (venta_total == costo_camion):
    print('No hubo ganancias ni pérdidas, salimos derechos')
else:
    perdida = -(venta_total - costo_camion)
    print(f'La pérdida fue de: {perdida:0.2f}')