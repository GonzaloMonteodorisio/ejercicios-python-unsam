# Abrir archivo para lectura
archivo_lectura = open('readme.txt', 'rt', encoding='utf8')
print(archivo_lectura.read())
# Leer maxbites
data = archivo_lectura.read(3) # ver ?????
print(data)
# Abrir archivo para escritura
archivo_escritura = open('writeme.txt', 'wt', encoding='utf8')
# Cerramos los archivos
archivo_lectura.close()
# Escribir un texto en el archivo
archivo_escritura.write(
'''Nuevo texto escrito, campeón!\nvamos por la copa!\nganamos!''')
archivo_escritura.close()
# Abrir con "with" para que cierre el archivo al ejecutar el bloque
with open('readme.txt', 'rt', encoding="utf8") as file:
    print('leyendo líneas 2')
    data = file.read()
    print(data)
# Leer línea por línea
with open('writeme.txt', 'rt', encoding='utf8') as file:
    print('leyendo líneas')
    # Ver por qué no entra al for in ???
    for line in file:
        print('estamos en la línea')
        print(line)
# Para escribir cadenas
with open('outfile', 'wt') as out:
    out.write

# Para escribir cadenas
with open('outfile.txt', 'wt', encoding='utf8') as out:
    out.write('Hello worlds\n')

# Redireccionar la salida del print (de la pantalla a un archivo)
with open('out_file.txt', 'wt', encoding='utf8') as file_out:
    # Hago un print indicánlode dónde imprimir utilizando el atributo "file"
    print('Hello world\n', file=file_out) 
# Leer archivo ubicado en otra carpeta
with open('../Data/camion.csv', 'rt', encoding='utf8') as file:
    data = file.read()

print(data)

#Para leer una archivo línea por línea, usá un ciclo for como éste:
with open('../Data/camion.csv', 'rt') as f:
        for line in f:
            # usamos "end=' '" para que se genere un espacio en blanco antes de cada palabra, después del '\n' de la anterior
            print(line, end = ' ')

# En ciertas ocasiones, puede pasar que quieras leer una sola línea de texto (por ejemplo, querés saltearte la primera línea del archivo que contiene los nombres de las columnas).
f = open('../Data/camion.csv', 'rt')
# next() me separa la primer línea de lo que le paso como parámetro y luego trabaja con las líneas siguientes
headers = next(f)
print(headers)

for line in f:
    print(line, end='')

f.close()



