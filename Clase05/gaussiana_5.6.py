import random 
# Con random.random() generamos valores aleatorios entre 0 y 1 con una distribución uniforme. En esa distribución, todos los valores posibles tienen la misma probabilidad de ser seleccionados. También es posible generar valores aleatorios con otras distribuciones. Una de las distribuciones más importantes es la distribución normal o Gaussiana.

# La distribución normal tiene dos parámetros, denominados media y desvío estándar y denotados usualmente con las letras griegas mu y sigma, respectivamente.

# Distribución normal

# La función random.normalvariate(mu,sigma) genera números aleatorios según esta distribución de probabilidades. Por ejemplo, usando mu = 0 y sigma = 1 podemos generar 6 valores aleatorios así:

for i in range(6):
        print(f'{random.normalvariate(0,1):.2f}', end=', ')