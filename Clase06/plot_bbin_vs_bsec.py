import matplotlib.pyplot as plt
import numpy as np
import random

def generar_lista(n, m):
    '''Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1'''
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    '''Devuelve un elemento aleatorio en el mismo rango de valores'''
    return random.randint(0, m-1)

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve, también la cantidad de comparaciones que huboque hacerse para llegar al resultado
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comparaciones = 0
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            comparaciones += 1
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
            comparaciones += 1
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            comparaciones += 1
    return pos, comparaciones

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k):
    n = 256
    lista = generar_lista(n, m)
    # Graficos de los resultados de estos experimentos para listas de largo entre 1 y 256.
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio_binario = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_promedio_secuencial = np.zeros(256)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)
        comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_promedio_binario,label = 'Búsqueda Binaria')
    plt.plot(largos,comps_promedio_secuencial,label = 'Búsqueda Secuencial')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.xlim(0,50) 
    plt.ylim(0,50) 
    plt.legend()
    plt.show()

def main():
    m = 10000
    k = 1000
    graficar_bbin_vs_bseq(m, k)
# main()