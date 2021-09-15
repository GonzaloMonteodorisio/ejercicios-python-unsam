import random
from tqdm import tqdm
# Probabilidad = Casos favorables / Casos posibles
def envido():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    mano = random.sample(naipes, k=3)

    # Condición para obtener 31:

    envido = 0
    if mano[0][1] == mano[1][1]:
        envido += 20
        if mano[0][0] <= 7:
            envido += mano[0][0]
        if mano[1][0] <= 7:
            envido += mano[1][0]
    suma2 = 0
    if mano[0][1] == mano[2][1]:
        suma2 += 20
        if mano[0][0] <= 7:
            suma2 += mano[0][0]
        if mano[2][0] <= 7:
            suma2 += mano[2][0]
    if suma2 > envido:
        envido = suma2
    suma3 = 0
    if mano[1][1] == mano[2][1]:
        suma3 += 20
        if mano[1][0] <= 7:
            suma3 += mano[1][0]
        if mano[2][0] <= 7:
            suma3 += mano[2][0]
    if suma3 > envido:
        envido = suma3

    return envido == 33

def main():
    N = 1000000
    G = sum([envido() for i in tqdm(range(N))])
    prob = G/N
    print(f'De {N} manos, {G} veces sumé 33 de envido.')
    print(f'Podemos aproximar la probabilidad de sacar 33 de envido en una mano a : {prob:.6f}.')
main()