import re
texto = 'Hoy es 6/8/2020. Mañana será 7/8/2020.'
print(texto)

print(re.findall(r'\d+/\d+/\d+', texto))
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto))