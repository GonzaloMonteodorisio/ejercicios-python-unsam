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

def contar_ejemplares(lista_arboles):
    contador_ejemplares = Counter()
    for arbol in lista_arboles:
        contador_ejemplares[arbol['nombre_com']] += 1
    return contador_ejemplares

cantidad_ejemplares_parque_general_paz = contar_ejemplares(parque_general_paz)

pprint(cantidad_ejemplares_parque_general_paz)

###############################################################
parque_los_andes = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
parque_centenario = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')

cantidad_ejemplares_parque_los_andes = contar_ejemplares(parque_los_andes)
cantidad_ejemplares_parque_centenario = contar_ejemplares(parque_centenario)

pprint(f"Los 5 ejemplares más comunes en el parque 'General Paz' son: {cantidad_ejemplares_parque_general_paz.most_common(5)}")
pprint(f"Los 5 ejemplares más comunes en el parque 'Los Andes' son: {cantidad_ejemplares_parque_los_andes.most_common(5)}")
pprint(f"Los 5 ejemplares más comunes en el parque 'Centenario' son: {cantidad_ejemplares_parque_centenario.most_common(5)}")

