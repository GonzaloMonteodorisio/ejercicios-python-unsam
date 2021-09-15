# El módulo "gzip" permite leer archivos comprimidos
import gzip
# Sin 'rt' leeríamos cadenas de bytes en vez de cadenas de caracteres
with gzip.open('../Data/camion.csv.gz', 'rt', encoding='utf8') as file:
    for line in file:
        print(line, end='')