import random

def cumpleanios():
    coincidencia = False
    dias = []
    for i in range(365):
        dias.append(i+1)
    # print(dias)
    dias_seleccionados = random.choices(dias, k=30)
    # print(dias_seleccionados)   
    repeticiones_dias = []
    for dia in dias:
        repeticiones_dias.append(dias_seleccionados.count(dia))
    # print(repeticiones_dias)
    nro_2_repeticiones = repeticiones_dias.count(2)
    # print(nro_2_repeticiones)
    if nro_2_repeticiones > 0:
        coincidencia = True
    return  coincidencia
def main():
    N = 1000000
    G = sum([cumpleanios() for i in range(N)])
    probabilidad = G/N
    print(probabilidad)
main()
