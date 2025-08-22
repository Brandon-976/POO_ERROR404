class Vehiculo:
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.en_marcha = False
    def arrancar(self):
        if self.en_marcha:
            print(f"El vehiculo {self.marca} {self.modelo} ya esta en marcha")
        else:
            self.en_marcha = True
            print(f"El vehiculo {self.marca} {self.modelo} ha arrancado")


class carro(Vehiculo):
     def __init__(self,marca,modelo,año):
         super().__init__(marca,modelo,año)
         self.tipo = "Carro"

     def terreno(self):
        print(f"El {self.tipo} {self.marca} {self.modelo} es adecuado para terrenos urbanos.")

     def acelerar(self):
         print(f"El {self.tipo} {self.marca} {self.modelo} está acelerando.")

class moto(Vehiculo):
     def __init__(self,marca,modelo,año):
         super().__init__(marca,modelo,año)
         self.tipo = "Moto"

     def truco(self):
         print(f"La {self.tipo} {self.marca} {self.modelo} realiza un truco impresionante.")

     def derrapar(self):
         print(f"La {self.tipo} {self.marca} {self.modelo} está derrapando.")

carro1 = carro("Toyota", "Corolla", 2020)
carro1.arrancar()
carro1.terreno()
carro1.acelerar()

moto1 = moto("Yamaha", "MT-07", 2021)
moto1.arrancar()
moto1.truco()
moto1.derrapar()
