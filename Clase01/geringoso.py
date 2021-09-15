# cadena = 'Geringoso'
# capadepenapa = ''
# for c in cadena:
#     # print(c)
#     if c == 'a':
#         capadepenapa = cadena.replace('a', 'apa')       
#     elif c == 'e':
#         capadepenapa = cadena.replace('e', 'epe')
#     elif c == 'i':
#         capadepenapa = cadena.replace('i', 'ipi')
#     elif c == 'o':
#         capadepenapa = cadena.replace('o', 'opo')
#     elif c == 'u':
#         capadepenapa = cadena.replace('u', 'upu')

# print(capadepenapa)

# Alternativa
cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    capadepenapa += c
    if c in 'aeiou':
        capadepenapa += 'p' + c
    elif c in 'AEIOU':
        capadepenapa += 'p' + c

print(capadepenapa)

# Ejemplo aparte sobre el método "enumerate"
for i,c in enumerate(cadena):
    print(i, c)