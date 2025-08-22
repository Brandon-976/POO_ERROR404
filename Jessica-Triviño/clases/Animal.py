
class Animal:
    def __init__(self, nombre, edad, vivo=True):
        self.nombre = nombre
        self.edad = edad
        self.vivo = vivo

    def comer(self):
        print(f"El animal {self.nombre} está comiendo")

    def caminar(self):
        pass

    def sonido(self):
        if self.vivo:
            print(f"El animal {self.nombre} emite un sonido característico")
        else:
            print(f"El animal {self.nombre} no hizo nada")


class Invertebrados(Animal):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad, vivo=True)
        self.tipo = tipo

    def caminar(self):
        if self.vivo:
            print(f"El animal {self.nombre} se arrastra")
        else:
            print(f"El animal {self.nombre} está muerto, no puede arrastrarse")


class Vertebrados(Animal):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad, vivo=True)
        self.tipo = tipo

    def caminar(self):
        if self.vivo:
            print(f"El animal {self.nombre} camina un paso")
        else:
            print(f"El animal {self.nombre} está muerto, no puede caminar")



animalito = Invertebrados("Mascota", 1, "Lombriz")
animalote = Vertebrados("Salvaje", 35, "Elefante")


animalote.vivo = False

animalito.comer()
animalote.comer()

animalito.caminar()
animalote.caminar()

animalito.sonido()
animalote.sonido()
