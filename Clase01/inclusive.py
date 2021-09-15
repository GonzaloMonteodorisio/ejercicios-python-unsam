# #frase = 'todos somos programadores de todo'
# #frase = 'Los hermanos sean unidos porque ésa es la ley primera'
# frase = '¿cómo transmitir a los otros el infinito Aleph?'
# #frase = 'Todos, tu también' # -> No funciona por la coma
# palabras = frase.split()
# print(palabras)
# for palabra in palabras:    
#     if palabra[-1] == 'o':
#         nueva_palabra = palabra[:-1] + 'e' 
#         indice = palabras.index(palabra)
#         palabras[indice] = nueva_palabra
#     if len(palabra) > 1:
#         if palabra[-2] == 'o':
#             nueva_palabra = palabra[:-2] + 'e' + palabra[-1:]
#             indice = palabras.index(palabra)
#             palabras[indice] = nueva_palabra

# frase_t = ' '.join(palabras)
# print(frase_t)

# Alternativa
frase = 'todos somos programadores de todo y no lo somos'
palabras = frase.split()
traduccion = []
for palabra in palabras:
    if palabra[-1] == 'o':
        nueva_palabra = palabra[:-1] + 'e' 
    # lazy evaluation
    elif len(palabra)>1 and palabra[-2] == 'o':
        nueva_palabra = palabra[:-2] + 'e' + palabra[-1:]
    else:
        nueva_palabra = palabra
    traduccion.append(nueva_palabra)

frase_t = ' '.join(traduccion)
print(frase_t)    