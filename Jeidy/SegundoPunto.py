# Crear tablero vacío, esta rellenado por guiones
tablero = [["-" for _ in range(5)] for _ in range(5)]

# Ubicacion del tesoro y de las trampas
tesoro = (0, 4)
trampas = [(1, 1), (3, 3), (4, 0)]

# Intentos
intentos = 5


print("Búsqueda del Tesoro")
while intentos > 0:
    for fila in tablero:
        print(" ".join(fila))
    print()

    fila = int(input("Fila (0-4): "))
    col = int(input("Columna (0-4): "))

    if (fila, col) == tesoro:
        print("¡Encontraste el tesoro!")
        tablero[fila][col] = "T"
        break
    elif (fila, col) in trampas:
        print("¡Caíste en una trampa!")
        tablero[fila][col] = "X"
        break
    else:
        print("Vacio")
        tablero[fila][col] = "O"
        intentos -= 1
        print("Te quedan", intentos, "intentos.\n")

for f, c in [tesoro] + trampas:
    if (f, c) == tesoro:
        tablero[f][c] = "T"
    else:
        tablero[f][c] = "X"

print("\nTablero final")
for fila in tablero:
    print(" ".join(fila))
