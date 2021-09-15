# Forma alternativa (con try - except) -> Ver ???

def buscar_precio(fruta):
    file = open('../Data/precios.csv', 'rt', encoding='utf8')
    fruta_en_listado = False
    while not fruta_en_listado:
        try:
            for line in file:
                row = line.split(',')
                if fruta in row:    
                    fruta_en_listado = True
                    print(f'El precio de un cajón de {fruta} es: {row[1]}')
                    break
        except:
            print(f'{fruta} no figura en el listado de precios.')
    
    file.close()

#buscar_precio('Naranja')
buscar_precio('Kinoto')