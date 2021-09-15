import copy
from incrementar import incrementar
def listar_secuencias(n):
    m = [0]*n
    secuencias = []
    secuencias += [m]
    while sum(m) != n:
        m = m.copy()
        secuencias += [incrementar(m)]   
    return secuencias
def main():
    secuencias = listar_secuencias(4)
    print(secuencias)
    print(len(secuencias))
main()