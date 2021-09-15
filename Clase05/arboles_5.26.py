import csv
import matplotlib.pyplot as plt
import numpy as np
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        tipos = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float ]
        arboleda = [dict(zip(encabezado,[func(val) for func,val in zip(tipos,row)])) for row in rows]
        # tipos_tupla = [float, int]
        tupla_altura_diametro = [(float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
        return tupla_altura_diametro

def scatter_hd(lista_de_pares):
    # print(lista_de_pares)
    lista = np.array(lista_de_pares)
    print(len(lista))
    # print(lista)
    d = lista.T[1]
    h = lista.T[0]
    N = 3255
    colors = np.random.rand(N)
    area = (7 * np.random.rand(N))**2  # 0 to 15 point radii
    plt.scatter(d, h, s=area, c=colors, alpha=0.7)
    plt.xlabel("diámetro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()
def main():
    tuplas_altura_diametro = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

    scatter_hd(tuplas_altura_diametro)
main()