import matplotlib.pyplot as plt
import numpy as np
# from busqueda_secuencial import busqueda_secuencial_
from experimento_secuencial import generar_lista
from experimento_secuencial_promedio import experimento_secuencial_promedio

m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
print(largos)
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.


for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)
print(comps_promedio)
# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()