from fileparse import parse_csv

def main():
    camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    print(camion)
main()