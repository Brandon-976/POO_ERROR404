#integrantes:
# BRANDON RIOS
# LUIA BUILES
# JESSICA MABEL TRIVINO
# JEIDY ANGELICA ZAPATA

import requests
import math

# ================== Algoritmos de ordenamiento ==================
def bubble_sort(lista, key, reverse=False):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if (lista[j][key] > lista[j+1][key]) ^ reverse:  # XOR para invertir
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def selection_sort(lista, key, reverse=False):
    n = len(lista)
    for i in range(n):
        idx = i
        for j in range(i+1, n):
            if (lista[j][key] < lista[idx][key]) ^ reverse:
                idx = j
        lista[i], lista[idx] = lista[idx], lista[i]
    return lista

def insertion_sort(lista, key, reverse=False):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i-1
        while j >= 0 and ((lista[j][key] > temp[key]) ^ reverse):
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = temp
    return lista

def merge_sort(lista, key, reverse=False):
    if len(lista) > 1:
        mid = len(lista)//2
        L = lista[:mid]
        R = lista[mid:]

        merge_sort(L, key, reverse)
        merge_sort(R, key, reverse)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if (L[i][key] < R[j][key]) ^ reverse:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista

def quick_sort(lista, key, reverse=False):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista)//2][key]
    left = [x for x in lista if (x[key] < pivot) ^ reverse]
    middle = [x for x in lista if x[key] == pivot]
    right = [x for x in lista if (x[key] > pivot) ^ reverse]
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)

def counting_sort(lista, key, reverse=False):
    if not lista:
        return lista
    max_val = max(p[key] for p in lista)
    min_val = min(p[key] for p in lista)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(lista)

    for p in lista:
        count[p[key] - min_val] += 1

    if reverse:
        for i in range(range_of_elements - 2, -1, -1):
            count[i] += count[i + 1]
    else:
        for i in range(1, range_of_elements):
            count[i] += count[i - 1]

    for p in reversed(lista):
        output[count[p[key] - min_val] - 1] = p
        count[p[key] - min_val] -= 1

    return output

def radix_sort(lista, key, reverse=False):
    if not lista:
        return lista
    
    # Encontrar el número máximo de dígitos
    max_val = max(item[key] for item in lista)
    max_digits = len(str(max_val))
    
    # Ordenar por cada dígito, desde el menos significativo
    for digit in range(max_digits):
        # Crear 10 buckets (0-9)
        buckets = [[] for _ in range(10)]
        
        for item in lista:
            # Obtener el dígito actual
            num = item[key]
            digit_val = (num // (10 ** digit)) % 10
            buckets[digit_val].append(item)
        
        # Reconstruir la lista
        lista = []
        for bucket in buckets:
            lista.extend(bucket)
    
    return lista if not reverse else lista[::-1]

def heap_sort(lista, key, reverse=False):
    def heapify(lista, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and ((lista[left][key] > lista[largest][key]) ^ reverse):
            largest = left
            
        if right < n and ((lista[right][key] > lista[largest][key]) ^ reverse):
            largest = right
            
        if largest != i:
            lista[i], lista[largest] = lista[largest], lista[i]
            heapify(lista, n, largest)
    
    n = len(lista)
    
    # Construir max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    
    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    
    return lista

def bucket_sort(lista, key, reverse=False):
    if not lista:
        return lista
    
    # Encontrar valores mínimo y máximo
    min_val = min(item[key] for item in lista)
    max_val = max(item[key] for item in lista)
    
    # Número de buckets (usamos la raíz cuadrada del tamaño)
    num_buckets = max(1, int(math.sqrt(len(lista))))
    bucket_range = (max_val - min_val + 1) / num_buckets
    
    # Crear buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribuir elementos en buckets
    for item in lista:
        if bucket_range == 0:
            bucket_index = 0
        else:
            bucket_index = min(int((item[key] - min_val) / bucket_range), num_buckets - 1)
        buckets[bucket_index].append(item)
    
    # Ordenar cada bucket (usamos insertion sort para buckets pequeños)
    for i in range(num_buckets):
        buckets[i] = insertion_sort(buckets[i], key, reverse)
    
    # Concatenar buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result if not reverse else result[::-1]

# ================== API ==================
def get_pokemons(limit=None):
    link = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(link)
    data = response.json()
    pokemons = []
    for p in data["results"]:
        # Traemos detalles de cada Pokémon
        details = requests.get(p["url"]).json()
        pokemons.append({
            "id": details["id"],
            "name": details["name"],
            "height": details["height"],
            "weight": details["weight"]
        })
    return pokemons

# ================== Main ==================
def main():
    print("=== Aplicación de Ordenamiento con Pokémon ===")

    # 1. Iniciar aplicación y consumir API
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100")
    data = response.json()
    pokemons = []
    for p in data["results"]:
        # Traemos detalles de cada Pokémon
        details = requests.get(p["url"]).json()
        pokemons.append({
            "id": details["id"],
            "name": details["name"],
            "height": details["height"],
            "weight": details["weight"]
        })
    print("\nPokémon sin ordenar:")
    for p in pokemons:
        print(p)

    # 2. Seleccionar algoritmo
    algoritmos = {
        "burbuja": bubble_sort,
        "seleccion": selection_sort,
        "insercion": insertion_sort,
        "merge": merge_sort,
        "quick": quick_sort,
        "counting": counting_sort,
        "radix": radix_sort,
        "heap": heap_sort,
        "bucket": bucket_sort
    }

    metodo = input(f"\nElige algoritmo {list(algoritmos.keys())}: ").lower()

    # 3. Seleccionar variable
    variable = input("Elige variable numérica (id, height, weight): ").lower()

    # 4. Orden asc/desc
    orden = input("Orden ascendente/descendente (asc/desc): ").lower()
    reverse = True if orden == "desc" else False

    if metodo in algoritmos and variable in ["id", "height", "weight"]:
        resultado = algoritmos[metodo](pokemons[:], variable, reverse)
        print("\nPokémon ordenados:")
        for p in resultado:
            print(p)
    else:
        print("Opción inválida.")

if __name__ == "__main__":

    main()
