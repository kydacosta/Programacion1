#GAJ 278080
# Simulación de MiniCalculadora Interactiva

while True:
    print("\n    CALCULADORA KYD   ")
    print("-- ELIGE UNA OPERACIÓN --")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingresa tu selección (1-5): ")

    if opcion == '1':
        a = int(input("Ingrese el primer número de la suma: "))
        b = int(input("Ingrese el segundo número de la suma: "))
        Rsuma = a + b
        print("El resultado de la suma es: ", Rsuma)
    elif opcion == '2':
        c = int(input("Ingrese el primer número de la resta: "))
        d = int(input("Ingrese el segundo número de la resta: "))
        Rresta = c - d
        print("El resultado de la suma es: ", Rresta)
    elif opcion == '3':
        e = int(input("Ingrese el primer número de la multiplicación: "))
        f = int(input("Ingrese el segundo número de la multiplicación: "))
        Rmult = e * f
        print("El resultado de la suma es: ", Rmult)
    elif opcion == '4':
        g = int(input("Ingrese el primer número de la división: "))
        h = int(input("Ingrese el segundo número de la división: "))
        Rdiv = g / h
        print("El resultado de la suma es: ", Rdiv)
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("opción invalida. Inténtelo de nuevo.")
