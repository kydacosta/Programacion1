#GAJ 278080

print ("=================================")
print("¡Asistente de Decisiones del Día!")
print ("=================================")

#def limpiar_entrada con input para que procese la respuesta del usuario con .strip() y .lower()

def limpiar_entrada(mensaje):
    return input(mensaje).strip().lower()

#Pedir el día de la semana
dia = limpiar_entrada("¿Qué día de la semana es hoy?: ")

#Pedir el clima actual del dia ingresado
clima = limpiar_entrada("¿Cuál es el clima de hoy? (Ej: soleado, lluvioso, nublado.): ")

#Variable para guardar la recomendación con "" para que el lenguaje lo sepa que esta destinado a contener texto.

recomendacion = ""

#ESTRUCTURA CON MATCH

#Se pone match para saber con cual dia hay coincidencia
match dia:
    #Si el caso fue "lunes":
    case "lunes":
        #if/elif/else anidados
        # == es un operador de igualdad. Los dos valores son iguales.
        if clima == "soleado":
            recomendacion = "¡Es lunes y esta soleado!, Es un buen momento para salir a correr."
        elif clima == "lluvioso":
            recomendacion = "Es lunes y está lloviendo. ¡Prepara tu café, es un buen momento para relajarse un poco!."
        elif clima == "nublado":
            recomendacion = "Lunes nublado. Aprovecha para organizar tu escritorio y concentrarte en tareas profundas."
        else:
            recomendacion = "Parece que ingresaste un clima no tan común. ¡Asi que disfruta de tu dia como lo desees!"


    case "viernes":
        if clima == "soleado":
            recomendacion = "¡Viernes soleado! Termina temprano y celebra el fin de semana con una salida con tus amigos."
        elif clima == "lluvioso":
            recomendacion = "Viernes lluvioso. ¡Noche de películas! Pide algo de cenar y relájate en casa."
        elif clima == "nublado":
            recomendacion = "Viernes nublado. Día perfecto para ir al gimnasio o algo de deporte y mover el cuerpo."
        else:
            recomendacion = "Parece que el clima que ingresaste no es estándar. ¡Pero ya es viernes! Disfruta la noche."

            
    case "sabado" | "domingo": 
        if clima == "soleado":
            recomendacion = "¡Fin de semana soleado!  Es ideal para un picnic o una excursión a la naturaleza."
        elif clima == "lluvioso":
            recomendacion = "Fin de semana lluvioso.  Quedarse en casa y leer un buen libro o jugar un videojuego es la mejor opción."
        elif clima == "nublado":
            recomendacion = "Fin de semana nublado.  Invita a amigos a casa o prueba una nueva receta de cocina."
        else:
            recomendacion = "El clima que ingresaste no es estándar para el fin de semana. ¡Aun así, relájate y diviértete!"

            
    case _: 
        if clima == "soleado":
            #El {dia.capitalize()} sirve para que ponga el dia y la primera letra la ponga en mayuscula.
            recomendacion = f"Es {dia.capitalize()} soleado.  Si estás entre semana, no olvides un breve descanso al aire libre."
        elif clima == "lluvioso":
            recomendacion = f"Es {dia.capitalize()} lluvioso.  Es un buen día para avanzar mucho en tus pendientes de la oficina/escuela."
        elif clima == "nublado":
            recomendacion = f"Es {dia.capitalize()} nublado.  Día tranquilo. Planea una cena sencilla para recargar energías."
        else:
            recomendacion = f"Es {dia.capitalize()}. No pude interpretar el clima, pero te recomiendo enfocarte en tus responsabilidades diarias."

print("\n--- Recomendación del Asistente ---")
print(recomendacion)
print("-----------------------------------")
