from locust import HttpUser, task, between

class ParkingUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def calcular_cobro(self):
        self.client.get(
            "/cobro",
            params={
                "minutos": 120,
                "vip": "false"
            }
        )

    @task
    def calcular_cobro_vip(self):
        self.client.get(
            "/cobro",
            params={
                "minutos": 120,
                "vip": "true"
            }
        )

    @task
    def calcular_cobro_mas_de_un_dia(self):
        self.client.get(
            "/cobro",
            params={
                "minutos": 1500,
                "vip": "false"
            }
        )

    @task
    def calcular_cobro_vip_mas_de_un_dia(self):
        self.client.get(
            "/cobro",
            params={
                "minutos": 1500,
                "vip": "true"
            }
        )