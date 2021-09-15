
def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    # Dentro de la función declaro la condición, el tipo de error y el mensaje de error. Cuando da error se corta la ejecución del código
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

preguntar_edad('Gonzalo')

# Mientras no se cumpla la condición del error se ejecuta "try"; si se cumple el error, se ejecuta "except"
for nombre in ['Pedro', 'Juan', 'Ale']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print('No ingresó una edad válida')

