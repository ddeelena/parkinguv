import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from parking.parking import calcular_cobro

scenarios("../features/parking.feature")


@pytest.fixture
def contexto():
    return {}


@given(parsers.parse("que un cliente estuvo {minutos:d} minutos en el parqueadero"))
def cliente_normal(contexto, minutos):
    contexto["minutos"] = minutos
    contexto["es_vip"] = False

@given(parsers.parse("que un cliente VIP estuvo {minutos:d} minutos en el parqueadero"))
def cliente_vip(contexto, minutos):
    contexto["minutos"] = minutos
    contexto["es_vip"] = True


@when("se calcula el cobro")
def calcular(contexto):
    contexto["resultado"] = calcular_cobro(
        contexto["minutos"],
        contexto["es_vip"]
    )


@then(parsers.parse("el total a pagar es de {valor:d} pesos"))
def validar_resultado(contexto, valor):
    assert contexto["resultado"] == valor