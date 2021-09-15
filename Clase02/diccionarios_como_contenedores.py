import csv
def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'r', encoding='utf8')
    rows = csv.reader(f)
    precios = {}
    for row in rows:
        try:
            precios[row[0]] = row[1]
            print(row)
        except IndexError:
            print('No se pueden leer los valores de una fila vacía')
    f.close()
    print(precios)

leer_precios('../Data/precios.csv')
