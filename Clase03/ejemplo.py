def columnas_palabras(p1, p2):
    if len(p1) != len(p2):
        p_mas_larga = max(len(p1), len(p2))
        p1 = p1.ljust(p_mas_larga)
        p2 = p2.ljust(p_mas_larga)
    for i, k in zip(p1, p2):
        print(i, k)
        
print(columnas_palabras("hola", "mundo"))
