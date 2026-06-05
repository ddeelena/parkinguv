# language: es

Característica: Cobro del parqueadero ParkingUv
    Como gerente del parqueadero ParkingUv
    Quiero calcular el cobro correctamente
    Para facturar a mis clientes

    Escenario: Cliente que estuvo menos de 30 minutos
        Dado que un cliente estuvo 20 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el total a pagar es de 0 pesos

    Escenario: Cliente que estuvo más de 30 minutos 
        Dado que un cliente estuvo 90 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el total a pagar es de 500 pesos

    Escenario: Cliente con descuento VIP
        Dado que un cliente VIP estuvo 90 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el total a pagar es de 400 pesos

    Escenario: Cobro máximo diario
        Dado que un cliente estuvo 1440 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el total a pagar es de 12000 pesos

    Escenario: Cliente con descuento VIP que estuvo más de 24 horas
        Dado que un cliente VIP estuvo 1500 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el total a pagar es de 9600 pesos
