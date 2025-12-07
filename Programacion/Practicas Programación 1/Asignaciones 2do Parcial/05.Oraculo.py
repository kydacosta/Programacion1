#GAJ 278080

import datetime

def calcular_elemento(año):
    ultimo_digito = año % 10
    if ultimo_digito == 0 or ultimo_digito == 1:
        elemento = "Metal"
    elif ultimo_digito == 2 or ultimo_digito == 3:
        elemento = "Agua"
    elif ultimo_digito == 4 or ultimo_digito == 5:
        elemento = "Madera"
    elif ultimo_digito == 6 or ultimo_digito == 7:
        elemento = "Fuego"
    else: 
        elemento = "Tierra"
    
    return elemento

def generar_prediccion(nombre, elemento, num_suerte, edad_actual):
    predicciones = {
        1: f"Hey! {nombre}! Tu conexion con el elemento {elemento} tienes {edad_actual} años te traerá gran sabiduría. Es un buen momento para aprender algo nuevo!",
        2: f"Veo que el elemento {elemento} guia tu camino, {nombre}. La fortuna sonrie a los valientes, atrevete a tomar ese riesgo en mente! Te espera una gran revelación a tus {edad_actual} años.",
        3: f"Tu número {num_suerte} y tu elemento {elemento} indican que este semestre si pasarás Programación {nombre}. Prepara tu mente para la abundancia!.",
        4: f"{nombre} El brillo que cargas les molestara a los demas, ya que tu elemento {elemento} te traerá exitos a tus {edad_actual} años, es cierto que ya no serás el mismo de antes."
    }
    return predicciones.get(num_suerte, "El Oraculo parpadea... error en tu número!")

def iniciar_oraculo():
    año_actual = 2025
    print("\n✦ ♰ Bienvenido al Oraculo Kyd! ♰ ✦")

    while True:
        respuesta = input("➛ ¿Deseas conocer tu destino? (Si-No):").strip().lower()
        if respuesta != "si":
            print("\n¡Cyaoo! Gracias por consultar el Oraculo. ¡Que la fortuna te acompañe!")
            break
        print("-" * 40)
        nombre = input("➛ 1. Dime tu nombre: ").strip()
        
        while True:
            try:
                año = int(input("➛ 2. ¿En que año naciste? (Ej. 2006): "))
                break
            except ValueError:
                print("¡Error! Por favor ingresa un año valido (numero entero).")
                
        while True:
            try:
                num_suerte = int(input("➛ 3. Elige tu número de la suerte (entre 1 y 4): "))
                if 1 <= num_suerte <= 4:
                    break
                else:
                    print("¡Error! El número debe ser entre 1 y 4.")
            except ValueError:
                print("¡Error! Por favor ingresa un número válido (entero).")
                
        edad = año_actual - año 
        elemento_magico = calcular_elemento(año)
        profecia = generar_prediccion(nombre, elemento_magico, num_suerte, edad)

        borde = "𒄬" * 70 
        print(f"\n{borde}")
        print("ʚ ¡TU PREDICCION HA SIDO REVELADA! ɞ")
        print(f"\nTu elemento Zodiacal es: 「{elemento_magico}」\n Edad: {edad} años.")
        print(f"\n{profecia}")
        print(f"\n{borde}")

if __name__ == "__main__":
    iniciar_oraculo()
