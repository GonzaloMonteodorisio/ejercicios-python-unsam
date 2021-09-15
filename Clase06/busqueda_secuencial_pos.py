def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos

def main():
    pos = busqueda_secuencial([1, 4, 5, 6], 6)
    print(pos)
main()