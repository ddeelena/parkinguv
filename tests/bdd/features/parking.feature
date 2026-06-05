# language: es
Caracteristica: Cobro del parqueadero ParkingUv
    Como gerente del parqueadero ParkingUv
    Quiero calcular el cobro correctamente
    Para facturar a mis clientes

    Escenario: Cliente que estuvo menos de 30 minutos
        Dado que un cliente estuvo 20 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el cobro debe ser de 0 pesos

    Escenario: Cliente que estuvo más de 30 minutos 
        Dado que un cliente estuvo 90 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el total a pgar es de 500

    Escenario: Cliente con descuento VIP
        Dado que un cliente VIP estuvo 90 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el total a pagar es 400

    Escenario: Cobro máximo diario
        Dado que un cliente estuvo 1440 minutos en el parqueadero
        Cuando se calcular el cobro
        Entonces el total a pagar es de 12000

    Escenario: Cliente con descuento VIP que estuvo más de 24 horas
        Dado que un cliente VIP estuvo 1500 minutos en el parqueadero
        Cuando se calcula el cobro
        Entonces el total a pagar es de 9600
