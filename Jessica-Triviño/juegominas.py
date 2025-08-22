import random
filas = 5
columnas = 5

tablero =[["-" for _ in range(columnas)] for _ in range(filas)]

posiciones = [(f, c) for f in range(filas) for c in range(columnas)]
random.shuffle(posiciones)

tesoro = posiciones.pop()
tablero[tesoro[0]][tesoro[1]] = "T"

for _ in range(3):
    trampa = posiciones.pop()
    tablero[trampa[0]][trampa[1]] = "X"

intentos = 5
encontrado = False

while intentos > 0 and not encontrado:
    print("\nTablero:")
    for fila in tablero:
        if encontrado or intentos == 0:
             print(" ".join(fila))
        else:
            print(" ".join(["-" if x in ["T", "X"] else x for x in fila]))
    try:
        fila_usuario = int(input("\nIngrese la fila (0-4): "))
        col_usuario = int(input("Ingrese la columna (0-4): "))
    except ValueError:
        print("por favor solo numero enteros")
        continue
    if tablero[fila_usuario][col_usuario] == "T":
        print("Por fin encontraste el tesoro")
        encontrado = True
        tablero[fila_usuario][col_usuario] = "T"
    elif tablero [fila_usuario][col_usuario]== "X":
            print("yaper jaja vuelve a intentarlo ¡juego finalizado!")
            break
    else:
         print("aca no fue (Vacio)")
         intentos -= 1
         print(f"tequedan {intentos} intentos")

print("\nTablero final:")
for fila in tablero:
     print(" ".join(fila))






