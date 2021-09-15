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
pprint(f"Estos son los datos de todos los árboles del parque 'General Paz': {parque_general_paz}")
print(len(parque_general_paz))