import costo_camion

def main():
    costo_total = costo_camion.costo_camion('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    print(costo_total)
main()
