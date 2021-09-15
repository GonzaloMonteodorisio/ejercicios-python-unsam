import csv

def parse_csv(nombre_archivo, select=['nombre', 'cajones', 'precio']):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(select, row))
            registros.append(registro)

    return registros

def main():
    camion = parse_csv('../Data/camion.csv')
    print(camion)
    cajones_retenidos = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'])
    print(cajones_retenidos)
main()