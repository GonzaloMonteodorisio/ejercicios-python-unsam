import sys
import csv
def costo_camion(nombre_archivo):
    f = open(nombre_archivo, encoding='utf8')

    rows = csv.reader(f)
    # next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
    headers = next(rows)
    costo_total = 0

    for row in rows:
        try:
            costo_total += float(row[1]) * float(row[2])
            #print(costo_total)
        except ValueError:
            print(f'El número de cajones no puede ser un string vacío', sys.exc_info()[0])

    f.close()

    return costo_total
    
print(len(sys.argv))
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv' 
costo = costo_camion(nombre_archivo)
print(f'Costo total: {costo}')