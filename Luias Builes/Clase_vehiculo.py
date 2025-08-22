class Vehiculo:

    # Método inicializador
    def __init__(self, marca, modelo, velocidad, encendido = False):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.encendido = encendido

    def encender(self):
        self.encendido = True
        print(f"El vehículo {self.marca} {self.modelo} está encendido")


    def mover(self):
        if self.encendido:
            print(f"El vehículo {self.marca} {self.modelo} se está moviendo a {self.velocidad} km/h")
        else:
            print(f"El vehículo {self.marca} {self.modelo} está apagado, no se puede mover")


class Carro(Vehiculo):

    def __init__(self, marca, modelo, velocidad, puertas):
        super().__init__(marca, modelo, velocidad)
        self.puertas = puertas

    def tocar_bocina(self):
        print(f"El carro {self.marca} {self.modelo} toca la bocina: ¡PIIII PIIII!")


class Moto(Vehiculo):

    def __init__(self, marca, modelo, velocidad, asientos):
        super().__init__(marca, modelo, velocidad)
        self.asientos = asientos

    def hacer_truco(self):
        if self.encendido:
            print(f"La moto {self.marca} {self.modelo} está haciendo un truco")
        else:
            print(f"La moto {self.marca} {self.modelo} está apagada, no puede hacer el truco")


# Crear objetos
carro = Carro("Toyota", "Corolla", 120, 4)
moto = Moto("Yamaha", "R3", 180, "2")


# Probar métodos

carro.encender()
carro.mover()
carro.tocar_bocina()


print("-------------------------------------------------------------")

moto.encender()
moto.mover()
moto.hacer_truco()




        