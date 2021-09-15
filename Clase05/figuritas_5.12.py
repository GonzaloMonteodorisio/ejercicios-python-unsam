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

def main():
    print(crear_album(670))
    print(album_incompleto(crear_album(670)))
    print(comprar_figu(670))
main()