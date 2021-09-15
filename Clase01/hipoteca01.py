# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
# Ejercicio 1.7: La hipoteca de David
# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
nro_mes = 0
adelanto = 1000

while saldo > 0:
    if nro_mes < 12:        
        saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto
        nro_mes += 1
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual 
        total_pagado = total_pagado + pago_mensual 
        nro_mes += 1


print('Total pagado', round(total_pagado, 2), nro_mes)