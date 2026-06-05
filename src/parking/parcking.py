import math 

MINUTOS_GRATIS = 30
PRECIO_POR_HORA = 500
TOPE_DIARIO = 12000
DESCUENTO_VIP = 0.20

def calcular_cobro(minutos_estacionado, es_vip=False):
    if minutos_estacionado <= MINUTOS_GRATIS:
        return 0
    
    horas_completas = math.ceil((minutos_estacionado - MINUTOS_GRATIS) / 60)
    cobro = horas_completas * PRECIO_POR_HORA

    if cobro > TOPE_DIARIO:
        cobro = TOPE_DIARIO

    if es_vip:
        cobro *= (1 - DESCUENTO_VIP)

    return int(cobro)

