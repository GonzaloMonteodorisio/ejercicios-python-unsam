import random as rdn
import numpy as np

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album

def album_incompleto(A):
    return 0 in A

def main():
    print(crear_album(670))
    print(album_incompleto(crear_album(670)))
main()