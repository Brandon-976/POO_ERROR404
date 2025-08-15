import random

# Comenzamos con el numero de intentos permitidos
N = 5
INTENTOS = 5

# Tapamos el tablero con "_"
oculto = [["-" for _ in range(N)] for _ in range(N)]
visible = [["-" for _ in range(N)] for _ in range(N)]

# Se colocan 3 trampas(X) y el tesoro (T)
posiciones = random.sample([(i, j) for i in range(N) for j in range(N)], 4)
tesoro = posiciones[0]
trampas = posiciones[1:]

oculto[tesoro[0]][tesoro[1]] = "T"
for r, c in trampas:
    oculto[r][c] = "X"

def imprimir(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

print("Búsqueda del Tesoro Encuentra el tesoro(T), pero ten cuidado con las trampas(X).")
print("Tienes 5 intentos.")
imprimir(visible)

# Se comienza el juego
intentos = INTENTOS
visitadas = set()

while intentos > 0:
    try:
        f = int(input("Fila (0-4): "))
        c = int(input("Columna (0-4): "))
    except ValueError:
        print("Ingresa un numero del 0 al 4.")
        continue

    if not (0 <= f < N and 0 <= c < N):
        print("Coordenada invalida. Intenta un numero del 0 al 4.")
        continue

    if (f, c) in visitadas:
        print("Ya usaste esta casilla. Deberias intentar con otra")
        continue

    visitadas.add((f, c))

    if oculto[f][c] == "T":
        visible[f][c] = "T"
        print(" ¡Felicidades! ¡Encontraste el tesoro!")
        break
    elif oculto[f][c] == "X":
        visible[f][c] = "X"
        print("Caíste en una trampa. Perdiste. Mejor suerte la proxima!")
        break
    else:
        visible[f][c] = "*"
        intentos -= 1
        print(f"Vacío. Te quedan {intentos} intento(s).")
        imprimir(visible)

# Final del juego y se revela las coordenadas en las que estaba el tesoro.
print(f"El tesoro estaba en {tesoro}")
imprimir(oculto)

