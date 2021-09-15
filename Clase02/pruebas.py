# Ejercicio 2.2 - Lectura de un archivo de datos
# import csv
# import gzip
# with gzip.open('../Data/camion.csv.gz', 'rt', encoding='utf8') as f:
#     data = csv.reader(f)
#     headers = next(f)
#     total = 0
#     for line in data:
#         total += int(line[1]) * float(line[2])
#     print(total)

# Ejercicio 2.14 - diccionario geringoso
# def diccionario_geringoso_lista(lista):
#     diccionario = {}
#     for palabra in lista:
#         capadepenapa = ''
#         for c in palabra:
#             capadepenapa += c
#             if c in 'aeiou':
#                 capadepenapa += 'p' + c
#             elif c in 'AEIOU':
#                 capadepenapa += 'p' + c

#         print(capadepenapa)
#         diccionario[palabra] = capadepenapa
#     print(diccionario)
# lista = ['banana', 'manzana', 'mandarina']
# diccionario_geringoso_lista(lista)

# Ejercicio 2.10
import csv
import sys

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, encoding='utf8')

    rows = csv.reader(f)
    # next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
    headers = next(rows)
    costo_total = 0

    for row in rows:
        try:
            print(row)
            costo_total += float(row[1]) * float(row[2])
            #print(costo_total)
        except ValueError:
            print(f'El número de cajones no puede ser un string vacío', sys.exc_info()[0])
    f.close()
    print(f'Costo total: {costo_total}')    
    return costo_total
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)





