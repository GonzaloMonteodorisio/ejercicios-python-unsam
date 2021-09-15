# Ejercicio 4.11: Extraer datos de un archivo CSV
# Saber usar combinaciones de comprensión de listas, diccionarios y conjuntos resulta útil para procesar datos en diferentes contextos. Aunque puede volverse medio críptico si no estás habituade. Acá te mostramos un ejemplo de cómo extraer columnas seleccionadas de un archivo CSV que tiene esas características. No es dificil cuando lo entendés, pero está muy concentrado todo.

# Primero, leamos el encabezado (header) del archivo CSV:

import csv
f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
print(rows)
headers = next(rows)
print(headers)

# Luego, definamos una lista que tenga las columnas que nos importan:
select = ['nombre', 'cajones', 'precio']

# Ubiquemos los índices de esas columnas en el CSV:
indices = [headers.index(ncolumna) for ncolumna in select]
print(indices)

# Y finalmente leamos los datos y armemos un diccionario usando comprensión de diccionarios:
row = next(rows)
print(row)

record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}   # comprensión de diccionario
print(record)
print(zip(select, indices))

camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
print(camion)