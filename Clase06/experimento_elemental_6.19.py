import random
from busqueda_secuencial import busqueda_secuencial_

def generar_lista(n, m):
    '''Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1'''
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    '''Devuelve un elemento aleatorio en el mismo rango de valores'''
    return random.randint(0, m-1)

def main():
    m = 10000
    n = 100
    lista = generar_lista(n, m)
    print(lista)
    # acá comienza el experimento
    x = generar_elemento(m)
    print(x)
    print(x in lista)
    comps = busqueda_secuencial_(lista, x)[1]
    print(comps)
# main()