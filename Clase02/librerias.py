# Librería "math"
import math
# Cálculo de la raiz cuadrada con el método .sqrt()
raiz = math.sqrt(100)
print(raiz)

# Librería urllib.request para abrir una url
import urllib.request
# usamos el método urlopen para abrir una url
url = urllib.request.urlopen('http://www.python.org/')
print(url)
# Leemos el HTML de la url solicitada
url_text = url.read()
print(url_text)