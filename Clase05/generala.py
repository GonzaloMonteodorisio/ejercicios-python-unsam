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
    generala = True
    longitud = len(tirada)
    for i in range(longitud):
        if i != 0:
            if tirada[i] != tirada[i-1]: # si dentro de mi tirada hay algún dado diferente al anterior declaro False al valor de generala
                generala = False
    if generala == False: 
        for i in range(6):
            repeticiones.append(tirada.count(i+1)) # si no hubo generala agrego a una lista la cantidad de veces que salió cada dado
    mas_repetido = None
    try:
        mas_repetido = repeticiones.index(max(repeticiones))+1 # defino al número más repetido como al primero que salió más veces
    except:
        pass
    for i in range(longitud):
        if tirada[i] == mas_repetido:
            dados_en_mesa.append(tirada[i]) # guardo en una lista de dados en mesa los dados que coincidan con el valor del más repetido
    for i in range(longitud-len(dados_en_mesa)): # tiro una cantidad de dados que va a ser la total menos los que quedaron en mesa
        tirada2.append(random.randint(1,6)) # guardo la segunda tirada
    # print(tirada2)
    for i in range(len(tirada2)): # verifico, en la segunda tirada si algún dado coincide con el valor de los que dejé en mesa y, en ese caso, lo agrega a la lista de dados en mesa
        if tirada2[i] == mas_repetido:
            dados_en_mesa.append(tirada2[i])
    if len(dados_en_mesa) == 5: # si tengo 5 dados en mesa declaro generala
        generala = True
    if generala == False: # si no tengo generala tiro por tercera vez y vuelvo a evaluar
        for i in range(longitud-len(dados_en_mesa)):
            tirada3.append(random.randint(1,6))
    for i in range(len(tirada3)):
        if tirada3[i] == mas_repetido:
            dados_en_mesa.append(tirada3[i])
    if len(dados_en_mesa) == 5:
        generala = True
    return generala # si hubo generala retorna True, si o, False

def main():
    N = 1000000
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N # estimo la probabilidad de sacar generala no servida con 1.000.000 de experimentos
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
# main()