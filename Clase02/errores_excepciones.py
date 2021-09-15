numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
        # Si no indico el tipo de error la ejecución terminamos atrapando todas las excepciones
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')

# Al correrlo va a detener la ejecución y permite rastrear la excepción leyendo el mensaje de error que imprime.
raise RuntimeError('Qué moco!')

# Alternativamente, esa excepción puede ser atrapada por un bloque try-except, pudiendo de esta forma evitar que el programa termine.
