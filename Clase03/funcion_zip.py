# La función zip toma múltiples secuencias y las combina en un iterador.
columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1]
pares = zip(columnas, valores)

for columna, valor in pares:
    print(f'({columna}, {valor})')
print(repr(pares))

# Creamos un diccionario con el método dict y zip partiendo de dos listas con similar cantidad las cuales combinamos
diccionario = dict(zip(columnas, valores))
print(diccionario)