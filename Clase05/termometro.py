import random
import copy
import numpy as np

T = 37.5

def medir_temp(n):
    mediciones = []
    for i in range(n):
        mediciones.append(37.5 + random.normalvariate(0,0.2)) # agrego a la lista mediciones n temperaturas modificadas según su desvío estandar en euna distribución normal
    np.save('../Data/temperaturas', mediciones) # guardo el vector con las temperaturas solicitadas en un archivo temperaturas.npy en la ruta pedida
    return mediciones

def resumen_temperatura(n): # función para plotear las temperaturas del ejercicio anterior
    mediciones = medir_temp(n)
    nro_maximo = max(mediciones)
    nro_minimo = min(mediciones)
    promedio = round(sum(mediciones)/n, 2)
    
    mediciones_ordenadas = copy.deepcopy(mediciones)
    mediciones_ordenadas.sort()
    mediana = 0
    if len(mediciones_ordenadas) % 2 == 0:
        mediana = mediciones_ordenadas[int(len(mediciones_ordenadas)/2)]
    else:
        mediana = mediciones_ordenadas[int((int(len(mediciones_ordenadas)/2) + int(len(mediciones_ordenadas)/2) +1)/2)]
    return (nro_maximo, nro_minimo, promedio, mediana)

def main():
    N = 999
    print(medir_temp(N))
# main()