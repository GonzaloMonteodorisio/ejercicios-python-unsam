import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy') # lee el archivo temperaturas.npy
    plt.hist(temperaturas,bins=100) # crea histograma con los datos de las temperaturas del archivo, ajustando los bins para mejor visualización del gráfico
    plt.show() # muestra el histograma

def main():
    plotear_temperaturas()
# main()