class Coche:
    def __init__(self, ruedas, aceleracion):
        self.ruedas = ruedas
        self.aceleracion = aceleracion

    def mostrar_detalles(self):
        print(f"Ruedas: {self.ruedas}")
        print(f"Aceleración: {self.aceleracion} m/s²")
    
    def frena(self):
        self.aceleracion -= 2


mi_coche = Coche(ruedas=4, aceleracion=3.5)

mi_coche.mostrar_detalles()

mi_moto_2=Coche(ruedas=2, aceleracion=2.5)

mi_moto_2.mostrar_detalles()

mi_moto_2.frena()

mi_moto_2.mostrar_detalles()