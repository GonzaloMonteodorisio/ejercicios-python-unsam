import csv
def leer_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding='utf8')
    rows = csv.reader(f)
    # next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
    headers = next(rows)
    camion = []
    for n_row, row in enumerate(rows):
        new_row = (str(row[0]), int(row[1]), float(row[2]))
        record = dict(zip(headers, new_row))
        camion.append(record)
    f.close()
    return camion

def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'r', encoding='utf8')
    rows = csv.reader(f)
    precios = {}
    for row in rows:
        try:
            precios[row[0]] = row[1]
        except IndexError:
            pass
    f.close()
    return precios

def hacer_informe(lista_cajones, dict_precios):
    lista_tuplas = []
    for line in lista_cajones:
        tupla = (line['nombre'], line['cajones'], line['precio'], round((float(dict_precios[line['nombre']]) - float(line['precio'])), 2))
        lista_tuplas.append(tupla)
    return lista_tuplas

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')            
    #########################################################
    print(f' {headers[0]:>9} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for linea in informe:
        precio_modificado = (f'${linea[2]}')
        print(f' {linea[0]:>9s} {(linea[1]):>10d} {precio_modificado:>10s} {round(linea[3], 2):>10.2f}')

def calcular_venta(lista, precios):
    venta_total = 0.0
    for producto in lista:
        venta_total += float(precios[producto['nombre']]) * int(producto['cajones'])
    return venta_total

def calcular_costo(lista):
    costo = 0.0
    for producto in lista:
        costo += int(producto['cajones']) * float(producto['precio'])
    return costo

def calcular_balance(venta, costo):
    balance = venta - costo
    return balance

def main():
    lista_camion = leer_camion('../Data/camion.csv')
    misPrecios = leer_precios('../Data/precios.csv')
    lista_informe = hacer_informe(lista_camion, misPrecios)
    imprimir_informe(lista_informe)
    venta = calcular_venta(lista_camion, misPrecios)
    print(venta)
    costo = calcular_costo(lista_camion)
    print(costo)
    balance = calcular_balance(venta, costo)
    print(round(balance, 2))
main()  