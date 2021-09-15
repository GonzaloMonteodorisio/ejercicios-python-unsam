import random as rdn
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album

def album_incompleto(A):
    incompleto = True
    if 0 not in A:
        incompleto = False
    return incompleto

def comprar_figu(figus_total):
    return rdn.randint(1,figus_total)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        album[figurita - 1] += 1
    return sum(album)

def experimento_figus(n_repeticiones, figus_total):
    figus_total_experimentos = []
    for i in range(n_repeticiones):
        total_figus_album = cuantas_figus(figus_total)
        figus_total_experimentos.append(total_figus_album)
    promedio = int(np.mean(figus_total_experimentos))
    return promedio

def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        paquete.append(comprar_figu(figus_total))
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)        
        for i, figurita in enumerate(paquete):
            album[figurita - 1] += 1
        paquetes += 1
    return paquetes

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop() - 1] = 1
            print(album>0)
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

def main():
    n_repeticiones = 100
    figus_total = 670
    figus_paquete = 5
    lista_paquetes = []
    for i in range(n_repeticiones):
        paquetes = cuantos_paquetes(figus_total, figus_paquete)
        lista_paquetes.append(paquetes)
    promedio = int(np.mean(lista_paquetes))
    print(promedio)

    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()
main()