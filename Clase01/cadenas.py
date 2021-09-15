cadena = ' Hello world '
# Indexación
print(cadena[2])
print(cadena[-5])
# Slice
print(cadena[:2])
print(cadena[2:])
print(cadena[2:4])
print(cadena[-5:])
# Longitud de una cadena
print(len(cadena))
# test de pertenencia (in, not in)
print('e' in cadena)
print('z' in cadena)
print('e' not in cadena)
print('z' not in cadena)
# replicación
print((cadena)* 3)
# strip
print(cadena.strip())
# Conversión entre mayúsculas y minúsculas
print(cadena.lower())
print(cadena.upper())
# Reemplazo de texto
print(cadena.replace('Hello', 'Hi'))
# .join() -> Une una lista de cadenas usando s como delimitador
espacio = ' '
lista = ['Pepe', 'tira', 'vaso']
print(espacio.join(lista))
# .split -> Parte la cadena en subcadenas según un delimitador
print(cadena.split(' '))

# Iteración sobre cadenas
# Ejemplo 1:
for c in cadena:
    print('Caracter:', c)
# Ejemplo 2:
contador = 0
for c in cadena:
    if c == 'o':
        contador += 1
        print('Hay', contador, "'o' en", cadena)
print('Hay, en total,', contador, "'o' en", cadena)
# f-strings
nombre = 'Naranja'
cajones = 100
precio = 91.1
# :espacios reservados para la parte entera.precisión decimal
print(f'{cajones} cajones de {nombre} a ${precio:7.3f}')

