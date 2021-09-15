import csv
from collections import Counter
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
parque_los_andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
parque_centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

# Inclinaciones
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones_especie = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones_especie.append(arbol['inclinacio'])
    return inclinaciones_especie

inclinaciones_jacaranda_parque_general_paz = obtener_inclinaciones(parque_general_paz, 'Jacarandá')

pprint(f"Las inclinaciones de los árboles de la especie 'Jacarandá' del parque 'General Paz' son: {inclinaciones_jacaranda_parque_general_paz}")


