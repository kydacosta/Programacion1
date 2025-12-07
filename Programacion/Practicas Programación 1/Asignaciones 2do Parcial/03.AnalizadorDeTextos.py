#GAJ278080
def analizar_texto():
    print("\n📝 Analizador de Textos Avanzado")

    texto = input("➡️ Ingresa el texto a analizar: ").lower().strip()

    letras_a_contar = []
    print("\n--- Vamos a contar tres letras ---")
    for i in range(3):
        while True:
            letra_input = input(f"Ingresa la letra #{i + 1}: ").lower().strip()
            if len(letra_input) == 1 and letra_input.isalpha():
                letras_a_contar.append(letra_input)
                break
            else:
                print("Por favor, ingresa solo una letra válida.")

    print("\n================ RESULTADOS ================")

    for letra in letras_a_contar:
        cantidad = texto.count(letra)
        print(f"La letra '{letra}' aparece {cantidad} veces en el texto.")

    palabras = texto.split()
    total_palabras = len(palabras)
    print(f"\nLa cantidad total de palabras es: {total_palabras}")

    if texto:
        primera_letra = texto[0]
        ultima_letra = texto[-1]
        print(f"Primera letra: '{primera_letra}'")
        print(f"Última letra: '{ultima_letra}'")
    else:
        print("El texto está vacío, no hay primera ni última letra.")

    texto_invertido = " ".join(palabras[::-1])
    print(f"\n Texto (Palabras) invertido: {texto_invertido}")

    contiene_python = "python" in texto
    if contiene_python:
        print("¡Enhorabuena! La palabra 'python' se encuentra en el texto.")
    else:
        print("La palabra 'python' no se encuentra en el texto.")
    
    print("============================================")

if __name__ == "__main__":
    analizar_texto()


