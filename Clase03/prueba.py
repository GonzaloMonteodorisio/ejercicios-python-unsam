import csv
from pprint import pprint
def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        dict_parque = []
        for n_lista, lista in enumerate(filas):
            dict_parques = dict(zip(encabezados, lista))
            if dict_parques['espacio_ve'] == parque:
                dict_parque.append(dict_parques)        
    return dict_parque
parque_general_paz = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

def especies(lista_arboles):
    lista_nombres_arboles = []
    for arbol in lista_arboles:
        lista_nombres_arboles.append(arbol['nombre_com'])
    set_nombres_arboles = set(lista_nombres_arboles)
    print(f"Set: {set_nombres_arboles}")
    return set_nombres_arboles
especies(parque_general_paz)

set_nombres_arboles_general_paz = especies(parque_general_paz)
# print(set_nombres_arboles_general_paz)

