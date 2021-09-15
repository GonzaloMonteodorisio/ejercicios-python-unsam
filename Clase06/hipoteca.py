saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
nro_mes = 1

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if nro_mes >= pago_extra_mes_comienzo and nro_mes <= pago_extra_mes_fin:        
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
        nro_mes += 1
    else:
        if (saldo * (1+tasa/12) - pago_mensual) < 0:
            print((saldo * (1+tasa/12) - pago_mensual) < 0)
            pago_mensual = - (saldo * (1+tasa/12) - pago_mensual)
            print(pago_mensual)
            saldo = 0
            print(saldo) 
            total_pagado = total_pagado + pago_mensual 
            nro_mes += 1
            print(nro_mes -1, round(total_pagado, 2), saldo)
        else:
            saldo = saldo * (1+tasa/12) - pago_mensual 
            total_pagado = total_pagado + pago_mensual 
            nro_mes += 1
            print(nro_mes -1, round(total_pagado, 2), saldo)
        print(nro_mes -1, round(total_pagado, 2), saldo)

print('Total pagado:', round(total_pagado, 2))
print(nro_mes - 1)