import fileparse

def leer_camion(nombre_archivo, select = None, types = None, has_headers = True):
    camion = fileparse.parse_csv(nombre_archivo, select, types, has_headers)
    return camion

def leer_precios(nombre_archivo, select = None, types = None, has_headers = True):
    precios = fileparse.parse_csv(nombre_archivo, select, types, has_headers)
    return precios
 
def hacer_informe(lista_cajones, dict_precios):
    lista_tuplas = []
    for line in lista_cajones:
        for tupla_precio in dict_precios:
            if line['nombre'] == tupla_precio[0]:
                tupla = (line['nombre'], line['cajones'], line['precio'], round((float(tupla_precio[1]) - float(line['precio'])), 2))
                lista_tuplas.append(tupla)
    return lista_tuplas

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')            
    #########################################################
    print(f' {headers[0]:>9} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for linea in informe:
        precio_modificado = (f'${linea[2]}')
        print(f' {linea[0]:>9s} {(linea[1]):>10d} {precio_modificado:>10s} {round(linea[3], 2):>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    precios = leer_precios(nombre_archivo_precios, select = ['nombre','precio'], types = [str, float], has_headers = False)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

def main():
    informe_camion('../Data/camion.csv', '../Data/precios.csv')
main()