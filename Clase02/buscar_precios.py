def buscar_precio(fruta):
    file = open('../Data/precios.csv', 'rt', encoding='utf8')
    fruta_en_listado = False
    for line in file:
        row = line.split(',')
        if fruta in row:    
            fruta_en_listado = True
            break

    if fruta_en_listado == True:
        print(f'El precio de un cajón de {fruta} es: {row[1]}')
    else:
        print(f'{fruta} no figura en el listado de precios.')

    file.close()
busqueda = input('Ingrese el nombre de una fruta o verdura con la inicial en mayúscula: ')
buscar_precio(busqueda)




