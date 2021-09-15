# Ejercicio 3.10
precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
}

# .items() -> devuelve un objeto de vista que muestra una lista de pares (clave, valor) -> dict_items
print(precios.items())
# .keys() -> devuelve un objeto de vista que muestra una lista de claves -> dict_keys
print(precios.keys())
# .values() -> devuelve un objeto de vista que muestra una lista de valores -> dict_values
print(precios.values())
# Devuelve una lista de tuplas (valor, clave)
lista_precios = list(zip(precios.values(),precios.keys()))
print(lista_precios)
# Devuelve la tupla de menor precio
print(min(lista_precios))
# Devuelve la tupla de mayor precio
print(max(lista_precios))
# Devuelve la lista de tuplas ordenada de menor a mayor
print(sorted(lista_precios))

# .zip() utilizado en más de dos listas de entrada
a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]
print(list(zip(a, b, c)))

# .zip() en el caso de una lista más corta que otras
a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
print(list(zip(a,b)))


