# Repasar preguntas extras
import random 

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    # print(tirada)
    dados_en_mesa = []
    repeticiones = []
    tirada2 = []
    tirada3 = []
    generala = True
    longitud = len(tirada)
    for i in range(longitud):
        if i != 0:
            if tirada[i] != tirada[i-1]:
                generala = False
    if generala == False:
        for i in range(6):
            repeticiones.append(tirada.count(i+1))
    # print(repeticiones)
    mas_repetido = None
    try:
        mas_repetido = repeticiones.index(max(repeticiones))+1
    except:
        pass
    # print(mas_repetido)
    for i in range(longitud):
        if tirada[i] == mas_repetido:
            dados_en_mesa.append(tirada[i])
    # print(dados_en_mesa)
    for i in range(longitud-len(dados_en_mesa)):
        tirada2.append(random.randint(1,6))
    # print(tirada2)
    for i in range(len(tirada2)):
        if tirada2[i] == mas_repetido:
            dados_en_mesa.append(tirada2[i])
    # print(dados_en_mesa)
    if len(dados_en_mesa) == 5:
        generala = True
    # print(generala)
    if generala == False:
        for i in range(longitud-len(dados_en_mesa)):
            tirada3.append(random.randint(1,6))
    # print(tirada3)
    for i in range(len(tirada3)):
        if tirada3[i] == mas_repetido:
            dados_en_mesa.append(tirada3[i])
    # print(dados_en_mesa)
    if len(dados_en_mesa) == 5:
        generala = True
    # print(generala)
    return generala

def main():
    N = 1000000
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
main()