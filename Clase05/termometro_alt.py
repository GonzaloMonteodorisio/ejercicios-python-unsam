import random
import copy
# Hagamos algún ejercicio sencillo antes de terminar. Supongamos que una persona se compra un termómetro que mide la temperatura con un error aleatorio de distribución normal con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la temperatura real de la persona es de 37.5 grados, simulá usando normalvariate() (con mu y sigma adecuados) n valores medidos por el termómetro. Escribí una función llamada medir_temp(n) que simule n mediciones y las devuelva en una lista.

# Escribí una función llamada resumen_temp(n) que realice una simulación de n temperaturas (usando la función medir_temp(n)) y devuelva una tupla con el valor máximo, el mínimo, el promedio y la mediana (en ese orden) de estas n mediciones. Guardá tu script en el archivo termometro.py.

# Para encontrar el máximo y mínimo podés usar y agrandar tu código de busqueda_en_listas.py o usar las primitivas max() y min() de Python. El promedio es la suma de los valores dividido su cantidad; podés programarla desde cero o usar la primitiva sum() y un cociente por n. Finalmente, la mediana de una cantidad impar de valores es el valor en la posición central cuando los datos están ordenados. Acá podés usar el método sort() de listas. En el caso de tratarse de una cantidad par de valores, la mediana se obtiene promediando los dos valores centrales. Y ya que estamos, ¿se te ocurre cómo encontrar los cuartiles?

T = 37.5

def medir_temp(n):
    mediciones = []
    for i in range(n):
        mediciones.append(37.5 + random.normalvariate(0,0.2))
    return mediciones

def resumen_temperatura(n):
    mediciones = medir_temp(n)
    print(mediciones)
    nro_maximo = max(mediciones)
    nro_minimo = min(mediciones)
    promedio = round(sum(mediciones)/n, 2)
    print(promedio)
    
    mediciones_ordenadas = copy.deepcopy(mediciones)
    mediciones_ordenadas.sort()
    print(mediciones_ordenadas)
    # Q1 = (n+1)/4
    # print(f'Q1: {Q1}')
    # Q3 = 3*(n+1)/4
    # print(f'Q3: {Q3}')
    mediana = 0
    if len(mediciones_ordenadas) % 2 == 0:
        mediana = mediciones_ordenadas[int(len(mediciones_ordenadas)/2)]
    else:
        mediana = mediciones_ordenadas[(int(len(mediciones_ordenadas)/2) + int(len(mediciones_ordenadas)/2) +1)/2]
    return (nro_maximo, nro_minimo, promedio, mediana)