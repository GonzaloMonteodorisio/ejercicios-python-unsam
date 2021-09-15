# Devuelve la suma de los primeros n enteros
def sumcount(n):

    total = 0
    while n > 0:
        total += n
        n -= 1
        print(total)
    return total

a = sumcount(100)
print(a)

# función "saludar"
nombre = input('Ingrese su nombre: ')
def saludar(nombre):
    print('Hola', nombre)

saludar(nombre)

help(saludar)

# Muestra el total de la compra
def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    # next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
    headers = next(f).split(',')
    costo_total = 0

    for line in f:
        row = line.split(',')
        print(row)
        costo_total += float(row[1]) * float(row[2])

    print('Costo total', costo_total)
    f.close()
    return costo_total
costo = costo_camion('../Data/camion.csv')
print('Costo total:',costo)
