import sys
import csv
def costo_camion(archivo):
    f = open(archivo)
    filas = csv.reader(f)
    encabezados = next(filas)
    costo_total = 0

    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            pass
    f.close()
    return costo_total

def main(): 
    costo_total = costo_camion('../Data/fecha_camion.csv')
    print(f'Costo total: {costo_total}')  
main()