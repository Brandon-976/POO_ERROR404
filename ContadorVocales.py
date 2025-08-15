#Contador de vocales: Contar cuantas vocales tiene una cadena ingresada por el usuario, almacenando en un diccionario y pudiendo escoger 
#después que tanto se repitió alguna vocal. El usuario ingresa la información y pregunta el número de veces que se repitió.

# Contador de vocales

texto = input("Ingrese una frase: ").lower()

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letra in texto:
    if letra in vocales:
        vocales[letra] += 1

for v in vocales:
    print(v, ":", vocales[v])

v = input("Vocal a consultar: ").lower()
print(vocales.get(v, "No es una vocal."))
