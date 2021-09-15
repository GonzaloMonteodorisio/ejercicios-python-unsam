# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso

def traduccion_geringoso(lista):
    lista_palabra_traduccion = []
    for cadena in lista:
        capadepenapa = ''
        for c in cadena:
            capadepenapa += c
            if c in 'aeiou':
                capadepenapa += 'p' + c
            elif c in 'AEIOU':
                capadepenapa += 'p' + c

        print(capadepenapa)
        lista_palabra_traduccion.append((cadena, capadepenapa))
    diccionario = dict(lista_palabra_traduccion)
    print('Mi diccionario es:', diccionario)
miLista = ['banana', 'manzana', 'mandarina']
traduccion_geringoso(miLista)