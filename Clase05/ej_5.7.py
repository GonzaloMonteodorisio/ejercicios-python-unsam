import numpy as np
# Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange(). Repetí el ejercicio usando linspace(). ¿Qué diferencia hay en el resultado?

# arange()
vector1 = np.arange(1, 20, 2)
print(vector1)
# linspace()
vector2 = np.linspace(1, 19, num=10, dtype=np.int64)
print(vector2)
