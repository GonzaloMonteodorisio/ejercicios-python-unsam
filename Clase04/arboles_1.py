import csv
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        tipos = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float ]
        arboleda = [dict(zip(encabezado,[func(val) for func,val in zip(tipos,row)])) for row in rows]
        return arboleda
        
def main():
    # print(leer_arboles('../Data/arbolado-en-espacios-verdes.csv'))
    print(leer_arboles('../Data/arbolado-en-espacios-verdes.csv')[0])
main()