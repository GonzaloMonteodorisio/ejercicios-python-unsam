import csv
from pprint import pprint
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        fila = next(filas)
        types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
        converted = [func(val) for func, val in zip(types, fila)]
        arboleda = dict(zip(encabezados, converted))
           
    return arboleda

def main():
    arboles = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    pprint(f"Estos son los datos de todos los árboles del archivo': {arboles}")
    print(len(arboles))
main()