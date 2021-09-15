import random

def generar_lista(n, m):
    '''Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1'''
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    '''Devuelve un elemento aleatorio en el mismo rango de valores'''
    return random.randint(0, m-1)

def main():
    lista = generar_lista(5, 20)
    print(lista)
    elemento = generar_elemento(6)
    print(elemento)
main()