import csv
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        tipos = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float ]
        arboleda = [dict(zip(encabezado,[func(val) for func,val in zip(tipos,row)])) for row in rows]
        return arboleda 

def medidas_de_especies(especies,arboleda):
    diccionario = { especie: [(float(arbol['altura_tot']), int(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies }

    return diccionario

def main():
    mi_arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    # print(leer_arboles('../Data/arbolado-en-espacios-verdes.csv'))
    # print(medidas_de_especies(especies, mi_arboleda))
    mis_medidas = medidas_de_especies(especies, mi_arboleda)
    print(mis_medidas)
    # print(medidas_de_especies(especies, mi_arboleda))
    print(len(mis_medidas['Eucalipto']))
    print(len(mis_medidas['Palo borracho rosado']))
    print(len(mis_medidas['Jacarandá']))
    print(len(mis_medidas))
main()