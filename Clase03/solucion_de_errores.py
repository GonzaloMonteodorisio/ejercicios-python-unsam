#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo SEMÁNTICO y estaba ubicado en el else y el acumulador. (Supuse que sólo importaba que contenga la vocal a en minúscula).
#    Lo corregí colocando el acumulador dentro del "else" y el "return False", al final, a la altura del "while".
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            i += 1
    return False

print(repr(tiene_a('UNSAM 2020')))
print(repr(tiene_a('abracadabra')))
print(repr(tiene_a('La novela 1984 de George Orwell')))

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de tipo SINTÁCTICO y estaba ubicado en la declaración de la función, el ciclo "while" y el condicional "if". Además, en el "if" la igualdad es de asignación, no de comparación. Y hay un "return Falso" que debería ser "return False".
#    Lo corregí colocando : al final de la declaración de la función, el ciclo "while" y la declaración "if". Cambiando el operador de asignación (=) por el de comparación (==) y cambiando el "return Falso" por "return False".
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(repr(tiene_a('UNSAM 2020')))
print(repr(tiene_a('La novela 1984 de George Orwell')))

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de tipo "SEMÁNTICO" y estaba ubicado en aplicarle el método len a una variable de tipo "number".
#    Lo corregí aplicandole el método str a la variable y guardándola en una nueva variable; luego, dentro del if, recorro los caracteres de la nueva expresión.
#    A continuación va el código corregido
def tiene_uno(expresion):
    string_expresion = str(expresion)
    n = len(string_expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if string_expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(repr(tiene_uno('UNSAM 2020')))
print(repr(tiene_uno('La novela 1984 de George Orwell')))
print(repr(tiene_uno(1984)))

#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo SEMÁNTICO y estaba ubicado en la función, le falta retornar la variable "c".
#    Lo corregí cambiando con un "return c" dentro de la función.
#    A continuación va el código corregido
def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
c = suma(a,b)
print(repr(f"La suma da {a} + {b} = {c}"))

#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo SEMÁNTICO y estaba ubicado en el lugar de declaración de "registro".
#    Lo corregí declarando "registro = {}" dentro del ciclo "for in", al aprincipio del mismo, en vez de declararlo antes de abrir el archivo, ya que, de esta manera, se pisan los valores generados.
#    A continuación va el código corregido
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(repr(camion))