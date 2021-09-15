import random
def medir_temp(n): #creo la funcion

    medidas = [] #lista vacía para agregar las medidas
    mu = 0 #media
    sigma = 0.2 #desvío estándar
  
    for i in range (n): #por cada elemento en el rango de n
        medicion = random.normalvariate(mu, sigma) + 37.5 #calcular números aleatorios 
        medidas.append(medicion) #agregalos a la lista
    return medidas

N = 100
temperatura = medir_temp(N) 
print(temperatura)
