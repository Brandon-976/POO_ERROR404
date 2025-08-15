# Pedir dimensiones
n = int(input("Número de filas: "))
m = int(input("Número de columnas: "))

# Recorrer la matriz horizontalmente
for i in range(n):          
    for j in range(m):      
        print(f"({i},{j})", end=" ")
    print()  
