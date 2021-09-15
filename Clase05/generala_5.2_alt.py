# Repasar preguntas extras
import random 

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    dados_en_mesa = []
    repeticiones = []
    tirada2 = []
    tirada3 = []
    generala = None
    longitud = len(tirada)
    for i in range(longitud):
        if i != 0:
            if tirada[i] != tirada[i-1]:
                generala = False
    if generala != False:
        generala = True
        return generala            
    else:
        for i in range(6):
            repeticiones.append(tirada.count(i+1))

    mas_repetido = None
    mas_repetido = repeticiones.index(max(repeticiones))+1    
    for i in range(longitud):
        if tirada[i] == mas_repetido:
            dados_en_mesa.append(tirada[i])
    for i in range(longitud-len(dados_en_mesa)):
        tirada2.append(random.randint(1,longitud-len(dados_en_mesa)+1))
    for i in range(len(tirada2)):
        if tirada2[i] == mas_repetido:
            dados_en_mesa.append(tirada2[i])
    if len(dados_en_mesa) == 5:
        generala = True
        return generala
    for i in range(longitud-len(dados_en_mesa)):
        tirada3.append(random.randint(1,longitud-len(dados_en_mesa)+1))
    for i in range(len(tirada3)):
        if tirada3[i] == mas_repetido:
            dados_en_mesa.append(tirada3[i])
    if len(dados_en_mesa) == 5:
        generala = True
        return generala
    return generala

def main():
    N = 1000000
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
main()
