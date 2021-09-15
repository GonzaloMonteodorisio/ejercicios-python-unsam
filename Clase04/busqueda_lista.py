def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1
    return pos

def main():
    busqueda_con_index([1, 4, 54, 3, 0, -1], 1)
    busqueda_con_index([1, 4, 54, 3, 0, -1], -1)
    busqueda_con_index([1, 4, 54, 3, 0, -1], 3)
    busqueda_con_index([1, 4, 54, 3, 0, -1], 44)
    busqueda_con_index([], 0)
main()