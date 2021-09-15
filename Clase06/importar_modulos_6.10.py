import fileparse
# help(fileparse)
# print(dir(fileparse))

def main():
    # camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    # print(camion)
    lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
    print(lista_precios)
    precios = dict(lista_precios)
    print(precios)
    precio_naranja = precios['Naranja']
    print(precio_naranja)
main()