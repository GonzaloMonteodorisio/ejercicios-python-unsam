# La función enumerate()
# La función enumerate agrega un contador extra a una iteración.

# Ejemplo 1
nombres = ['Edmundo', 'Juana', 'Rosita']
for i, nombre in enumerate(nombres):
    print(i, '-', nombre)

print('Fin ejemplo 1')

# Ejemplo 2
with open('../Data/camion.csv', encoding='utf8') as f:
    next(f)
    for nline, line in enumerate(f, start=1):
        print(nline, '-', line)


