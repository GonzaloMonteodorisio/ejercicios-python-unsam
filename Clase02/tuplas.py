import csv
f = open('../Data/camion.csv', encoding='utf8')
filas = csv.reader(f)
next(filas)

costo = 0
for fila in filas:
    t = (fila[0], int(fila[1]), float(fila[2]))
    nombre, cajones, precio = t
    nueva_t = (nombre, cajones * 2, precio)
    costo += t[1] * t[2]
    print(t)
    print(nueva_t)
    print(nombre)
    print(costo)
print(costo)