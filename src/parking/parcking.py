import math 

MINUTOS_GRATIS = 30
PRECIO_POR_HORA = 500
TOPE_DIARIO = 12000
DESCUENTO_VIP = 0.20

def calcular_cobro_base(minutos_estacionado):
    if minutos_estacionado <= MINUTOS_GRATIS:
        return 0

    horas = math.ceil(
        (minutos_estacionado - MINUTOS_GRATIS) / 60
    )

    return min(
        horas * PRECIO_POR_HORA,
        TOPE_DIARIO
    )


def calcular_cobro(minutos_estacionado, es_vip=False):
    cobro = calcular_cobro_base(minutos_estacionado)

    if es_vip:
        cobro = calcular_cobro_vip(cobro)

    return int(cobro)

def calcular_cobro_vip(cobro):
    return int(cobro * (1 - DESCUENTO_VIP))

