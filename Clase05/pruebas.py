import csv
import os
import matplotlib.pyplot as plt 
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "rt", encoding = "utf8") as f:

        rows = csv.reader(f)
        encabezado = next(rows)
        
        tipos = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float ]
        arboleda = [dict(zip(encabezado,[func(val) for func,val in zip(tipos,row)])) for row in rows]
        H=[float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
        return H
def main():
    pass
    # print(leer_arboles("../Data/arbolado-en-espacios-verdes.csv"))
    # nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    # print(nombre_archivo)
    # arboleda = leer_arboles(nombre_archivo)
    # altos = [comprensión de listas]
    # plt.hist(altos,bins=...)
main()
