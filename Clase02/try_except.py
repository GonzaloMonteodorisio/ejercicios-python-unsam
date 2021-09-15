# Ejemplo 1
import sys
def division(dividendo, divisor):
    resultado = dividendo/divisor
    return resultado

try:
    num = int(input('Ingrese un número entero distinto de cero: '))
    print(f'El resultado de la división es: {division(1, num)}')
except (ValueError, TypeError, IndexError):
    print('Tienes un error al introducir el número.')
    print('El error fue:', sys.exc_info()[0])
except ZeroDivisionError:
    print('El divisor no puede ser 0')
    print('El error fue:', sys.exc_info()[0])

# Ejemplo 2