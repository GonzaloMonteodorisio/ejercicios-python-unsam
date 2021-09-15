import csv
f = open('../Data/camion.csv')
filas = csv.reader(f)
next(filas)

fila = next(filas)

d = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }
print('Mi diccionario es:',d)

cost = d['cajones'] * d['precio']
print('El costo es de:',cost)

d['cajones'] = 75
d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345
print('Mi diccionario modificado es:',d)

# Ej. 2.13 - Más operaciones sobre diccionarios
for k in d:
    print('k=', k) # devuelva las claves

for k in d:
    print(k, '=', d[k]) # devuelve los valores de cada clave

# .items()
items = d.items()
print('Mi lista de tuplas clave - valor es:', items)

for k, v in d.items():
    print(k, '=', v)

# list()
print('Mi lista de claves es:',list(d))

# .keys()
print('Mi lista de claves es:',d.keys())

#dict()
print('Mi nuevo diccionario es:', dict(items))