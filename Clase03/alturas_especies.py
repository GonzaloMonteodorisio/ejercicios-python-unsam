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

def obtener_alturas(lista_arboles, especie):
    alturas_especie = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas_especie.append(float(arbol['altura_tot']))
    return alturas_especie

lista_alturas_jacaranda_parque_general_paz = obtener_alturas(parque_general_paz, 'Jacarandá')

lista_alturas_jacaranda_parque_los_andes = obtener_alturas(parque_los_andes, 'Jacarandá')

lista_alturas_jacaranda_parque_centenario = obtener_alturas(parque_centenario, 'Jacarandá')

# Lista alturas
pprint(f"Las alturas de los árboles de la especie 'Jacarandá' del parque 'General Paz' son: {lista_alturas_jacaranda_parque_general_paz}")

pprint(f"Las alturas de los árboles de la especie 'Jacarandá' del parque 'Los Andes' son: {lista_alturas_jacaranda_parque_los_andes}")

pprint(f"Las alturas de los árboles de la especie 'Jacarandá' del parque 'Centenario' son: {lista_alturas_jacaranda_parque_centenario}")

# Altura máxima
pprint(f"Las altura máxima de los árboles de la especie 'Jacarandá' del parque 'General Paz' es: {max(lista_alturas_jacaranda_parque_general_paz)}")

pprint(f"Las altura máxima de los árboles de la especie 'Jacarandá' del parque 'Los Andes' es: {max(lista_alturas_jacaranda_parque_los_andes)}")

pprint(f"Las altura máxima de los árboles de la especie 'Jacarandá' del parque 'Centenario' es: {max(lista_alturas_jacaranda_parque_centenario)}")

# Prmedio
pprint(f"El promedio de las alturas de los árboles de la especie 'Jacarandá' del parque 'General Paz' es: {round(float(sum(lista_alturas_jacaranda_parque_general_paz)/len(lista_alturas_jacaranda_parque_general_paz)), 2)}")

pprint(f"El promedio de las alturas de los árboles de la especie 'Jacarandá' del parque 'Los Andes' es: {round(float(sum(lista_alturas_jacaranda_parque_los_andes)/len(lista_alturas_jacaranda_parque_los_andes)), 2)}")

pprint(f"El promedio de las alturas de los árboles de la especie 'Jacarandá' del parque 'Centenario' es: {round(float(sum(lista_alturas_jacaranda_parque_centenario)/len(lista_alturas_jacaranda_parque_centenario)), 2)}")