
# next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con l
# as líneas siguientes
def buscar_precio(fruta):
    print(fruta)
    f = open('../Data/precios.csv', 'rt', encoding='utf8')
    for line in f:
        row = line.split(',')       
        try:
            print('except')
            if(fruta not in line):
                print(fruta, 'no figura en la lista de precios')            
        except: 
            print('try')
            if ('Naranja' in line):
                print('El precio del cajon de', row[0], 'es', row[1])
            
    f.close()

buscar_precio('Naranja')
buscar_precio('Kinoto')