import csv
from collections import Counter
from os import pipe
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

# pprint(f"Las inclinaciones de los árboles de la especie 'Jacarandá' del parque 'General Paz' son: {inclinaciones_jacaranda_parque_general_paz}")

# lista de árboles de una especie determinada
def especies(lista_arboles):
    set_nombres_arboles = set()
    for arbol in lista_arboles:
        set_nombres_arboles.add(arbol['nombre_com'])
    return set_nombres_arboles
especies(parque_general_paz)

set_nombres_arboles_general_paz = especies(parque_general_paz)
set_nombres_arboles_los_andes = especies(parque_los_andes)
set_nombres_arboles_centenario = especies(parque_centenario)

# Especie más inclinada en promedio
def especie_promedio_mas_inclinada(lista_arboles):
    especies_parque = especies(lista_arboles)
    dict_promedios_inclinacion = {}
    for especie in especies_parque:
        inclinaciones_especie = obtener_inclinaciones(lista_arboles, especie)
        inclinaciones_especie_numero = []
        for inclinaciones in inclinaciones_especie:
            inclinaciones_especie_numero.append(int(inclinaciones))
        promedio_inclinaciones_especie = round(sum(inclinaciones_especie_numero)/len(inclinaciones_especie_numero), 2)
        # pprint(promedio_inclinaciones_especie)
        dict_promedios_inclinacion[especie] = promedio_inclinaciones_especie
    max_key = max(dict_promedios_inclinacion, key=lambda key: dict_promedios_inclinacion[key])
    especie_maxima_inclinacion = (max_key, dict_promedios_inclinacion[max_key])
    return especie_maxima_inclinacion
especia_maxima_inclinacion_los_andes = especie_promedio_mas_inclinada(parque_los_andes)

pprint(f"La especie de máxima inclinación , en promedio, del parque 'Los Andes' es: {especia_maxima_inclinacion_los_andes[0]} y su inclinación promedio es de: {especia_maxima_inclinacion_los_andes[1]}")

