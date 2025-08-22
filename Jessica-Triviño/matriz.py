filas = 4
columnas = 5

matriz = []
numero = 1

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(numero)
        numero += 1
    matriz.append(fila)

print("Así queda mi matriz:") 
for fila in matriz:
    for valor in fila:
        print(valor, end="\t") 
    print()

print("\nRecorrido:")
for i in range(filas):
    if i % 2 == 0:
        for j in range(columnas):
            print(matriz[i][j], end=" ")
    else:
        for j in range(columnas -1,-1, -1):
            print(matriz[i][j], end=" ")
            


