import csv
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        tipos = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float ]
        arboleda = [dict(zip(encabezado,[func(val) for func,val in zip(tipos,row)])) for row in rows]
        # tipos_tupla = [float, int]
        tupla_altura_diametro = [(float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
        return tupla_altura_diametro
        
def main():
    print(leer_arboles('../Data/arbolado-en-espacios-verdes.csv'))
# main()