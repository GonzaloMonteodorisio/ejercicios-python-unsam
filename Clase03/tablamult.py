numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'{numeros[0]:8d} {numeros[1]:>3d} {numeros[2]:>3d} {numeros[3]:>3d} {numeros[4]:>3d} {numeros[5]:>3d} {numeros[6]:>3d} {numeros[7]:>3d} {numeros[8]:>3d} {numeros[9]:>3d}')

print('--------------------------------------------')

tablas = {}
for i in range(10):
    tabla = []
    for j in range(10):
        resultado = 0
        for k in range(j):
            resultado += i
        tabla.append(resultado)
        tablas[i] = tabla
        
for k, c in tablas.items():
    print(f'{k:d}: {c[0]:>5d} {c[1]:>3d} {c[2]:>3d} {c[3]:>3d} {c[4]:>3d} {c[5]:>3d} {c[6]:>3d} {c[7]:>3d} {c[8]:>3d} {c[9]:>3d}')


