def buscar_u_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista:  # recorremos los elementos de la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
        i += 1       
    return pos

def buscar_n_elemento(lista, e):
    cantidad = 0     
    for z in lista:  # recorremos los elementos de la lista
        if z == e:   # si encontramos a e
            cantidad += 1       
    return cantidad 

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    if not(lista):
        print('lista vacía')
        return None
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = float("-inf") # Lo inicializo en -inf para contemplar, también, números negativos
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def minimo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = float("inf") # Lo inicializo en inf para contemplar, también, números positivos
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m

def main():
    # print(buscar_u_elemento([1,2,3,2,3,4],1))
    # print(buscar_u_elemento([1,2,3,2,3,4],2))
    # print(buscar_u_elemento([1,2,3,2,3,4],3))
    # print(buscar_u_elemento([1,2,3,2,3,4],5))   

    # print(buscar_n_elemento([1,2,3,2,3,4],1))
    # print(buscar_n_elemento([1,2,3,2,3,4],2))
    # print(buscar_n_elemento([1,2,3,2,3,4],3))
    # print(buscar_n_elemento([1,2,3,2,3,4],5))

    # print(maximo([1,2,7,2,3,4]))
    # print(maximo([1,2,3,4]))
    # print(maximo([-5,4]))
    # print(maximo([-5,-4]))    

    print(minimo([1,2,7,2,3,4]))
    print(minimo([1,2,3,4]))
    print(minimo([-5,4]))
    print(minimo([-5,-4])) 
main()