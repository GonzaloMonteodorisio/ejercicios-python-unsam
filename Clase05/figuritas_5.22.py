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
def main():
    probabilidad = 0.9
    figus_total = 670
    cantidad_figus_paquete = 5
    paquetes = 0
    paquetes = cuantos_paquetes(figus_total, cantidad_figus_paquete)
    N = int(paquetes/probabilidad)
    print(N)
main()