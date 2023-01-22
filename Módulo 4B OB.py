class Vehiculo:
    color = None
    ruedas = None
    puertas = None

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None
    automovil = None

    def __init__(self, automovil):
        self.velocidad = "80 km/h"
        self.cilindrada = "1.600 cc"
        self.automovil = automovil

p = Coche("Nissan Almera")
print("Veamos estas caracteristicas del siguiente coche:")
print(p.automovil)
print(p.velocidad)
print(p.cilindrada)
