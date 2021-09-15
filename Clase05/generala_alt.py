#ejercicio 4.7
#GENERALA NO SERVIDA
from collections import Counter
import random
#función 1: guardo la lista de 5 dados aleatorios en la lista DADOS
def tirar():
    dados=[]
    for i in range(5):
        dados.append(random.randint(1,6))
    return dados
dados=tirar()
# print(dados)
 
#función 2
 
def es_generala(dados):
    dados=tirar()
    if min(dados)== max(dados): #si son todos iguales, return True
        return True
    else:
       numero, cantidad = Counter(dados).most_common()[0] #guardo en variable numero y cantidad data del mas repetido
       lista_repetidos=[numero for i in range(cantidad)] #hago una lista con los más repetidos
        #para iterar 2 veces
       para_tirar = (5 - len(lista_repetidos)) #identifico cuántos dados debería tirar en la tirada 2 y 3
       dados_no_rep=[] #lista vacía par guardar las tiradas 2 y 3
            # for r in dados: #itero sobre ellos
            #     if r!=numero: #si algún elemento de la tirada inicial es distinto a mi dado + repetido, lo agrego
            #         dados_no_rep.append(r)
       tiros=[0,1]
       for t in tiros:
            for i in range(para_tirar):
               dados_no_rep.append(random.randint(1,6)) #agrego los dados a una lista nueva
               #print(dados)
            for a in dados_no_rep:
                #for b in lista_repetidos:#itero sobre cada elemento de dados_no_rep
                    if a==numero and len(lista_repetidos)<=5:
                        lista_repetidos.append(a)
                    elif a!=numero and len(dados_no_rep)<=5:
                        para_tirar2= (5 - len(lista_repetidos))
                        dados_no_rep.append(random.randint(1,6))
 
                # if dado== numero: #si dado es igual al repetido, lo agrego a la lista
                #    lista_repetidos.append(dado)
                # if dado != numero: #si dado es distinto a repetido, tiro de nuevo
                #     dados_no_rep[a]=random.randint(1,6)
            #lista_repetidos.append(dados_no_rep)
            if max (dados) == min (dados):
                    return True
            else:
                    return False
N = 1000000
g = sum ([es_generala(tirar()) for i in range(N)])
prob = (g/N)
print (f'Tire {N} veces, de las cuales {g} saque generala')
print (f'podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}')