import random as rdn
import numpy as np

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64) # creo un álbum vacío con la cantidad de figuritas pasadas como parámetro (nparray lleno de 0)
    return album

def album_incompleto(A):
    incompleto = True
    if 0 not in A: # evaluó si hay algún 0 en el array de album; en caso contrario, el album estaría lleno y la variable incompleto toma el valor de False
        incompleto = False
    return incompleto

def comprar_figu(figus_total):
    return rdn.randint(1,figus_total) # compro una figurita al azar dentro de la cantidad pasada por parámetro

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    while album_incompleto(album): 
        figurita = comprar_figu(figus_total) # mientras el álbum esté incompleto sigo comprando figuritas
        album[figurita - 1] += 1 # voy sumando de uno en uno el valor de la figurita que me tocó según la cantidad que tenga de la misma, en su posición dentro del array album
    return sum(album)

def experimento_figus(n_repeticiones, figus_total):
    figus_total_experimentos = []
    for i in range(n_repeticiones):
        total_figus_album = cuantas_figus(figus_total)
        figus_total_experimentos.append(total_figus_album) # agrego el valor de cuantas figuritas tuve que comprar para llenar cada álbum para cada experimento realizado a una lista
    promedio = int(np.mean(figus_total_experimentos)) # saco el promedio de esa lista
    return promedio

def main():
    N = 100
    figus_total = 670
    print(experimento_figus(N, figus_total)) # calculo el promedio de cuantas figuritas tendría que comprar para llenar un álbum de 670 figuritas realizando 100 experimentos
# main()