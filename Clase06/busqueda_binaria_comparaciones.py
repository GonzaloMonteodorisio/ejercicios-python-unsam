def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve, también la cantidad de comparaciones que huboque hacerse para llegar al resultado
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comparaciones = 0
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            comparaciones += 1
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
            comparaciones += 1
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            comparaciones += 1
    return pos, comparaciones

def main():
    # posicion, comparaciones = busqueda_binaria([1, 3, 5], 5, verbose = True)
    # posicion, comparaciones = busqueda_binaria([1, 3, 5], 6, verbose = True)
    posicion, comparaciones = busqueda_binaria([1, 3, 5], 1, verbose = True)
    print(posicion)
    print(comparaciones)
# main()