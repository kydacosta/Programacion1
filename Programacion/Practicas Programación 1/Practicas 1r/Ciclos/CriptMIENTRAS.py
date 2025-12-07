#CriptoMonedas de pseudocodigo en python.
#GAJ 278080

monto = int(input("Ingrese el monto disponible para invertir: "))

inversion = 0
contador = 0

while monto >= inversion:
    inversion = int(input("¿Cuánto desea invertir del monto?: "))
    if monto >= inversion:
        print("Usted ha realizado una compra.")
        contador =+1
        SD = monto - inversion
        print("El total de compras es: ", contador)
        print("Su saldo restante es: ", SD)
    else:
        print("Ingrese un monto menor o igual a: ", monto)
