# ejercicio 1.8
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra = 1000
total_pagado = 0.0
mes = 0
while saldo > 0:
    mes += 1
    if mes <= 12:
        a_pagar = pago_mensual + pago_extra
    else:
        a_pagar = pago_mensual
    saldo = saldo * (1+tasa/12) - a_pagar
    total_pagado += a_pagar
print('Total pagado', round(total_pagado, 2))
print('Meses', mes)