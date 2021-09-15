import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
# Lo podés guardar en “filename.npy” con:
np.save('filename', a)

# Y lo podés cargar con np.load() para reconstruir tu vector.
b = np.load('filename.npy')
print(b)

# En formato de texto plano, lo podés guardar como .csv o .txt con np.savetxt.
#cPor ejemplo, si tenés este vector:
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(csv_arr)

# lo podés guardar en un archivo .csv con nombre “new_file.csv” así:
np.savetxt('new_file.csv', csv_arr)

# Y lo podés cargar fácilmente usando loadtxt():
mi_csv = np.loadtxt('new_file.csv')
print(mi_csv)

# Las funciones savetxt() y loadtxt() aceptan parámetros adicionales para especificar el encabezado y los delimitadores. Si bien los archivos de texto son sencillos para compartir, los archivos .npy (y .npz) son más pequeños y se leen más rápidamente.