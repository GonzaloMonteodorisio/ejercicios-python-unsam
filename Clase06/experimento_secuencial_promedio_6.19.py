from busqueda_secuencial import busqueda_secuencial_
from experimento_secuencial import generar_elemento, generar_lista

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def main():
    m = 10000
    n = 100
    k = 1000
    lista = generar_lista(n, m)
    print(lista)
    comparaciones_promedio = experimento_secuencial_promedio(lista, m, k)
    print(comparaciones_promedio)
main()