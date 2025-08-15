n = int(input("Número de filas: "))
m = int(input("Número de columnas: "))

matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        valor = int(input(f"Ingrese el valor para posición ({i},{j}): "))
        fila.append(valor)
    matriz.append(fila)

for fila in matriz:
    print(fila)

print("Recorrido en zig-zag:")
for i in range(n):
    if i % 2 == 0:  
        for j in range(m):
            print(matriz[i][j], end=" ")
    else:  
        for j in range(m-1, -1, -1):
            print(matriz[i][j], end=" ")
    print()  