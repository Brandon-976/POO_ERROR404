class Animal:

    # Metodo inicializador
    def __init__(self, nombre, edad, vivo = True):
        self.nombre = nombre
        self.edad = edad 
        self.vivo = vivo

    def comer(self):
        print(f"El animal {self.nombre}, esta comiendo")

    def caminar(self):
        if self.vivo:
            print(f"El animal {self.nombre}, se arrastra")
        else:
            print(f"El animal {self.nombre}, esta muerto, no puede arrastrarse")

    def sonido(self):   
        if self.vivo:
            print(f"El animal {self.nombre}, esta haciendo sonidos")
        else:
            print(f"El animal {self.nombre}, esta muerto, no puede hacer sonidos")


class invertebrados(Animal):
        
     # Metodo inicializador
    def __init__(self, nombre, edad, tipo):
            super().__init__(nombre, edad, vivo = True)
            self.tipo = tipo

    def caminar(self):
            if self.vivo:
                print(f"El animal {self.nombre}, esta caminando")
            else:
                print(f"El animal {self.nombre}, esta muerto, no puede caminar")

# Guardar info
animalito = invertebrados("mascota", 1, "Lombriz")
animalote = Animal("Salvaje", 35, "Elefante")

animalote.vivo = True  

# Hacer consulta
print(animalito.edad)
print(animalote.edad)
animalito.caminar()
animalote.caminar()
animalito.comer()
animalote.comer()
animalito.sonido()
animalote.sonido()


