import csv
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types = [str, float, str, str, float, float, float, float, int]

converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
fecha = record['date']
fecha_lista = fecha.split('/')
fecha_types = [int, int, int]
fecha_lista_converted = tuple([func(val) for func, val in (zip(fecha_types, fecha_lista))])

def main():
    print(converted)
    print(record)
    print(fecha)
    print(fecha_lista)
    print(fecha_lista_converted)
main()