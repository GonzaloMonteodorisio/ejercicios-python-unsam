import informe_funciones

def costo_camion(archivo, select = None, types = None, has_headers = True):
    camion = informe_funciones.leer_camion(archivo, select, types, has_headers)
    costo_total = 0
    for dict in camion:
        costo_total += dict['cajones'] * dict['precio']
    return costo_total
    
def main(): 
    # costo_total = costo_camion('../Data/fecha_camion.csv')
    # print(f'Costo total: {costo_total}')  
    costo_total = costo_camion('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    print(costo_total)
# main()