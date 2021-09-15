nombres = [ 'Rosita', 'Manuel', 'Luciana' ]
mas_nombres = ['Pepe', 'Mónica']

print(nombres + mas_nombres)
nombres.append('Rocío')
print(nombres)
print(nombres[2])
print(nombres[-1])
# cambiar un valor de la lista
nombres[1] = 'Oscar'
print(nombres)
# insertar un valor a la lista en determinada posición
nombres.insert(2, 'Iratxe')
print(nombres)
print(len(nombres))
print('Rosita' in nombres)
print('Facundo' in nombres)
print(nombres * 3)
nombres.remove('Oscar')
print(nombres)
del nombres[2]
print(nombres)
nombres.sort()
print(nombres)
nombres.sort(reverse=True)
print(nombres)

nueva_lista = sorted(nombres)
print(nueva_lista)