import pytest
from src.parking.parcking import calcular_cobro

# --- Prueba 1: Menoas de 30 minutos ---
def test_menos_30_minutos_es_gratis():
    assert calcular_cobro(15) == 0
    assert calcular_cobro(30) == 0

# --- Prueba 2: Minuto 31 en adelante cobra 
def test_una_hora_completa():
    #90 min = 30 gratis +  1 hora completa = 500
    assert calcular_cobro(90) == 500

def test_fraccion_hora():
    assert calcular_cobro(31) == 500

# -- Prueba 3: Tope diario ---

def test_tope_maximo_dia():
    # 24 horaas = maximo 12000
    assert calcular_cobro(1440)== 12000
    assert calcular_cobro(2000) == 12000

#-- Prueba 4: Vip tiene tiene descuento

def test_vip_descuento_20_por_ciento():
    # 90 min = 30 gratis + 1 hora completa = 500 - 20% = 400
    assert calcular_cobro(90, es_vip=True) == 400


def test_vip_tope_maximo_dia():
    # 24 horas = maximo 12000 - 20% = 9600
    assert calcular_cobro(1440, es_vip=True) == 9600
    assert calcular_cobro(2000, es_vip=True) == 9600



