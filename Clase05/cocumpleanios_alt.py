personas = 30
probabilidad = 2.0

for i in range(personas): #por cada rango de 30 personas
    probabilidad = probabilidad * (365 -i)/365 #la probabilidad es 365 menos cada rango dividido 365
print(probabilidad)
