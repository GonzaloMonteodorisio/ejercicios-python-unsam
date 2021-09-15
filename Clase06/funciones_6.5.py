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

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

def main():
    # informe_camion('../Data/camion.csv', '../Data/precios.csv')
    # informe_camion('../Data/camion2.csv', '../Data/precios.csv')
    files = ['../Data/camion.csv', '../Data/camion2.csv']
    for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()
main()