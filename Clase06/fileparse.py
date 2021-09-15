import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo, encoding="utf8") as f:
        filas = csv.reader(f)
        registros = []
        # Lee los encabezados del archivo si los tiene
        if has_headers:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                # si se seleccionaron tipos, parsear los valores segun esos types
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                registro = dict(zip(encabezados, fila)) # arma un diccionario con los encabezados como claves y las filas como valor
                registros.append(registro) # genera una lista de diccionarios

        else: # en caso de que el archivo no tenga headers
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                registro = (fila[0], fila[1]) # arma una tupla con los valores de la fila
                registros.append(registro) # genera una lista de tuplas

    return registros

def main():
    camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    print(camion)
# main()