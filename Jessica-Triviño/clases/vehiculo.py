class Vehiculo:
    def __init__(self, nombre, color, ruedas, velocidad):
        self.nombre = nombre
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad

    def encender(self):
        print(f"El vehículo {self.nombre} encendido.")

    def acelerar(self):
        print(f"El vehículo {self.nombre} su velocidad es de {self.velocidad} km/h.")

    def frenar(self):
        print(f"El vehículo {self.nombre} se detiene")



class Carro(Vehiculo):
    def frenar(self):
        print(f"El carro {self.nombre} se detuvo")



class Moto(Vehiculo):
    def frenar(self):
        print(f"La moto {self.nombre} se detuvo")



carro1 = Carro("Toyota", "Rojo", 4, 180)
moto1 = Moto("Yamaha", "Negra", 2, 120)
carro1.encender()
moto1.encender()
carro1.acelerar()
moto1.acelerar()
carro1.frenar()
moto1.frenar()
