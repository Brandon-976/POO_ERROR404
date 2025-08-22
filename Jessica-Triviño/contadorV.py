texto = input ("ingrese el texto:").lower()

contador_vocales ={
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}
for letra in texto:
    if letra in contador_vocales:
        contador_vocales[letra] += 1

        print("encontramos")
        for vocal, cantidad in contador_vocales.items():
            print(f"{vocal}: {cantidad}")

    vocal_buscada = input("ingrese una vocal").lower()
    if vocal_buscada in contador_vocales:
        print(f"la vocal'{vocal_buscada}'se repite{contador_vocales[vocal_buscada]}veces.")
    else:
        print("no ingreso una vocal valida.")
        
