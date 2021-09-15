def invertir_lista(lista):
    invertida = []
    i = len(lista)
    j = -1
    while i > 0:       
        for e in lista: # Recorro la lista
            #agrego el elemento e al principio de la lista invertida            
            if lista[j] == e:          
                invertida.append(e)
                i -= 1
                if j > -len(lista):
                    j -= 1                
    return invertida
invertir_lista([1, 2, 3, 4, 5])
def main():
    print(invertir_lista([1, 2, 3, 4, 5]))
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
# main()