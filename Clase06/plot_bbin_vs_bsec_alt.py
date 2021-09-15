# Ejercicio 6.20: Búsqueda binaria vs. búsqueda secuencial
import matplotlib.pyplot as plt
import numpy as np
from experimento_secuencial import generar_lista, generar_elemento
from busqueda_binaria_comparaciones import busqueda_binaria
from experimento_secuencial_promedio import experimento_secuencial_promedio

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def main():
    m = 10000
    n = 256
    lista = generar_lista(n, m)
    k = 10
    comparaciones_promedio = experimento_binario_promedio(lista, m, k)
    print(comparaciones_promedio)

    # Graficos de los resultados de estos experimentos para listas de largo entre 1 y 256.

    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    print(largos)
    comps_promedio_binario = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_promedio_secuencial = np.zeros(256)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)
        comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
    print(comps_promedio_binario)
    print(comps_promedio_secuencial)
    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_promedio_binario,label = 'Búsqueda Binaria')
    plt.plot(largos,comps_promedio_secuencial,label = 'Búsqueda Secuencial')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.xlim(0,20) 
    plt.ylim(0,10) 
    plt.legend()
    plt.show()
main()