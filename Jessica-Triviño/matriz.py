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
    print("\t".join(map(str, fila)))

print("\nRecorrido:")
for suma in range(filas + columnas  -1):
    if suma % 1 == 0:
        i = min(suma, filas - 1)
        j = suma - i
        while i >= 0 and j < columnas:
            print(matriz[i][j], end=" ")
            i -= 1 
            j += 1
    else:
        j = min(suma, columnas - 1)
        i = suma - j
        while j >= 0 and i < filas:
            print(matriz[i][j], end=" ")
            i -= 1
            j += 1
            


