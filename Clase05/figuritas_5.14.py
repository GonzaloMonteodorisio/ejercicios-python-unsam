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

def main():
    N = 1000
    figus_total = 6
    lista_resultados = list([cuantas_figus(figus_total) for i in range(N)])
    # print(lista_resultados)
    promedio = int(np.mean(lista_resultados))
    print(promedio)
main()