import random

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
        generala = True
        longitud = len(tirada)
        for i in range(longitud):
            if i != 0:
                if tirada[i] != tirada[i-1]:
                    generala = False
        return generala

def main():
    N = 1000000
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
main()