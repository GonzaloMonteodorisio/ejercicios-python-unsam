import random as rdn
import numpy as np

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

def main():
    # N = 1000
    figus_total = 670
    cantidad_figus_paquete = 5
    paquete = []
    for i in range(cantidad_figus_paquete):
        paquete.append(comprar_figu(figus_total))
    print(paquete)
main()