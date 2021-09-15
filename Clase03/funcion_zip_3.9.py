import csv
# Aparear encabezados con una fila de datos
f = open('../Data/camion.csv')
filas = csv.reader(f)
encabezados = next(filas)
fila = next(filas)
primera_lista = list(zip(encabezados, fila))
print(primera_lista)

