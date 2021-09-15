# Reducción de secuencias
s = [1, 2, 3, 4]
print(sum(s))

print(min(s))

print(max(s))

t = ['Hello', 'World']
print(max(t))

# Ciclos sobre enteros
lista_numeros = []
for i in range(100):
    # Imprime los índices desde el cero, sin incluir el último valor
    lista_numeros.append(i)
print(f'* Mi lista de números desde el índice 0 al 100 es: {lista_numeros}')

# Otro ejemplo con range([comienzo,] fin [, paso])
nueva_lista_numeros = []
for k in range(50,100,2):
    nueva_lista_numeros.append(k)
print(f'* Mi lista de números desde el índice 0 al 100 es: {nueva_lista_numeros}')

