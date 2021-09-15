s = {
    'nombre': 'Naranja',
    'cajones': 100,
    'precio': 91.1
}

print('{nombre:>10s} {cajones:10d} {precio:10.2f}'.format_map(s))

