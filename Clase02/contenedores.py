import csv
# Listas -> Usá listas cuando el orden de los datos importe. Acordate de que las listas pueden contener cualquier tipo de objeto. Por ejemplo, una lista de tuplas.
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]

camion[0]            # ('Pera', 100, 490.1)
camion[2]            # ('Limon', 150, 83.44)
# Construcción de una lista
# Cómo armar una lista desde cero.

registros = []  # Empezamos con una lista vacía

# Usamos el .append() para agregar elementos
registros.append(('Pera', 100, 490.10))
registros.append(('Naranja', 50, 91.3))

registros = []  # Empezamos con una lista vacía

with open('../Data/camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))

# Diccionarios -> Los diccionarios son útiles si vamos a querer buscar rápidamente (por claves).
precios = {
   'Pera': 513.25,
   'Limon': 87.22,
   'Naranja': 93.37,
   'Mandarina': 44.12
}
# Así podemos buscar datos:

precios['Naranja']
93.37
precios['Pera']
513.25

# Construcción de diccionarios
# Ejemplo de armado de un diccionario desde cero.

precios = {} # Empezamos con un diccionario vacío

# Agregamos elementos
precios['Pera'] = 513.25
precios['Limon'] = 87.22
precios['Naranja'] = 93.37
# Un ejemplo de cómo armar un diccionario a partir del contenido de un archivo.

precios = {}  # Empezamos con un diccionario vacío

f = open('../Data/precios.csv', 'r', encoding='utf8')
rows = csv.reader(f)
for row in rows:
    try:
        precios[row[0]] = float(row[1])
    except IndexError:
        print('Ésta es una línea vacía')
print(precios)

# Verificar si existe una clave en un diccionario
def verificar_clave(clave, diccionario):
    if clave in diccionario:
        print("Existe la clave", clave,  "en el diccionario") 
    else:
        print("No existe la clave", clave,  "en el diccionario")

verificar_clave('Ciruela', precios)
verificar_clave('Pepino', precios)

# Claves compuestas
# Casi cualquier valor puede usarse como clave en un diccionario de Python. La principal restricción es que una clave debe ser de tipo inmutable. 

feriados = {
  (1, 1) : 'Año nuevo',
  (1, 5) : 'Día del trabajador',
  (13, 9) : "Día del programador",
}
# Luego, podemos acceder al diccionario así:

print(feriados[(1, 5)])

# Conjuntos
# Un conjunto es una colección de elementos únicos sin orden y sin repetición.

citricos = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así:
citricos = set(['Naranja', 'Limon', 'Mandarina'])
# Los conjuntos son útiles para evaluar pertenencia.

print(citricos)
set(['Naranja', 'Limon', 'Mandarina'])
print('Naranja' in citricos)
print('Manzana' in citricos)

# Los conjuntos también son útiles para eliminar duplicados.

nombres = ['Naranja', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Banana']

unicos = set(nombres)
print(unicos)
# unicos = {'Manzana', 'Banana', 'Naranja', 'Pera'}
# Más operaciones en conjuntos:

citricos.add('Banana')        # Agregar un elemento
citricos.remove('Limon')    # Eliminar un elemento
print(citricos)
# s1 | s2                 # Unión de conjuntos s1 y s2
# s1 & s2                 # Intersección de conjuntos
# s1 - s2       

