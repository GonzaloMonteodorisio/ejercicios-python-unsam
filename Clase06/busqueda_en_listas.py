def busqueda_lineal_lordenada(lista,e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
        if z > e:
            break    # y salimos del ciclo
    return pos

def main():
    posicion = busqueda_lineal_lordenada([1,2,3,4,5], 4)
    print(posicion)
main()