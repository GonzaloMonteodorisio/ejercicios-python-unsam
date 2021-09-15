import csv
import matplotlib.pyplot as plt
import numpy as np
def leer_arboles(nombre_archivo): # utilizo la función leer_arboles de unidades anteriores
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        tipos = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float ]
        arboleda = [dict(zip(encabezado,[func(val) for func,val in zip(tipos,row)])) for row in rows]
        tupla_altura_diametro = [(float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
        return tupla_altura_diametro # retorna una lista de tuplas (altura, diámetro) de todos los Jacarandá de la lista pasada (en este ejercicio aplica para todos los parques)

def scatter_hd(lista_de_pares):
    lista = np.array(lista_de_pares) # convierto la lista de tuplas (altura, diámetro) en un ndarray
    d = lista.T[1] # creo una nueva lista con todos los valores en el índice 1 de mis vectores; o sea, una lista de diámetros
    h = lista.T[0] # creo una nueva lista con todos los valores en el índice 0 de mis vectores; o sea, una lista de alturas
    N = len(lista_de_pares) # longitud de mi lista
    colors = np.random.rand(N) # genero colores de forma aleatoria para mejor visualización de los puntos de mi gráfico
    area = (7 * np.random.rand(N))**2  # seteo un area adecuada para cada uno de mis puntos
    plt.scatter(d, h, s=area, c=colors, alpha=0.7) # genero un gráfico de puntos pasándole la lista de diámetros en el eje x, la lista de alturas en el eje y, el área de cada punto o círculo, el color o colores, y la nitidez del punto 
    plt.xlabel("diámetro (cm)") # genero una leyenda para el eje x
    plt.ylabel("alto (m)") # genero una leyenda para el eje y
    plt.title("Relación diámetro-alto para Jacarandás") # genero un título para el gráfico
    plt.show() # muestro el gráfico (concluyo relación lineal entre el diámetro y la altura)

def main():
    tuplas_altura_diametro = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    scatter_hd(tuplas_altura_diametro)
# main()