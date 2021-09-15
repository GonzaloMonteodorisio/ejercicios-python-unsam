import csv
from collections import Counter
from os import pipe
from pprint import pprint
import operator

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

# Especie con el ejemplar más inclinado
def especimen_mas_inclinado(lista_arboles):
    dict_inclinacion_maxima_especie = {}
    for arbol in lista_arboles:
        lista_inclinaciones_especie = obtener_inclinaciones(lista_arboles, arbol['nombre_com'])
        lista_inclinaciones_especie_numero = []
        for inclinacion in lista_inclinaciones_especie:
            inclinacion_numero = int(inclinacion)
            lista_inclinaciones_especie_numero.append(inclinacion_numero)
        dict_inclinacion_maxima_especie[arbol['nombre_com']] = max(lista_inclinaciones_especie_numero)
    
    max_key = max(dict_inclinacion_maxima_especie, key=lambda key: dict_inclinacion_maxima_especie[key])
    especie_maxima_inclinacion = (max_key, dict_inclinacion_maxima_especie[max_key])
            
    return especie_maxima_inclinacion

especimen_mas_inclinado_general_paz = especimen_mas_inclinado(parque_general_paz)
especimen_mas_inclinado_los_andes = especimen_mas_inclinado(parque_los_andes)
especimen_mas_inclinado_centenario = especimen_mas_inclinado(parque_centenario)

pprint(f"El especimen más inclinado en el parque 'General Paz' es:  {especimen_mas_inclinado_general_paz[0]} y su inclinación es de: {especimen_mas_inclinado_general_paz[1]}")

pprint(f"El especimen más inclinado en el parque 'Los Andes' es:  {especimen_mas_inclinado_los_andes[0]} y su inclinación es de: {especimen_mas_inclinado_los_andes[1]}")

pprint(f"El especimen más inclinado en el parque 'Centenario' es:  {especimen_mas_inclinado_centenario[0]} y su inclinación es de: {especimen_mas_inclinado_centenario[1]}")