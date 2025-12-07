#GAJ27080

import random

def generar_respuesta():
    respuestas_magicas = [
        "Sí", 
        "No", 
        "Tal vez", 
        "Pregunta más tarde", 
        "Definitivamente", 
        "Definitivamente no", 
        "No cuentes con eso", 
        "Claro que sí", 
        "Claro que no", 
        "No lo creo", 
        "Es seguro", 
        "Probablemente", 
        "No estoy seguro"
    ]
    
    # Selecciona una respuesta al azar de la lista
    respuesta = random.choice(respuestas_magicas)
    return respuesta

def iniciar_bola_magica():
    print("\n🎱 Bienvenido a la Bola Mágica de Python. ¡Haz tu pregunta!")
    
    while True:
        pregunta = input("\nHaz tu pregunta (o escribe 'salir'): ").strip()
        
        if pregunta.lower() == "salir":
            print("\n¡Adiós! La magia siempre está aquí si la necesitas.")
            break
        
        if not pregunta:
            print("Pregunta algo para que te responda.")
            continue
            
        respuesta_oraculo = generar_respuesta()
        
        print("-" * 50)
        print(f"Pregunta: {pregunta}")
        print(f"🎱 La bola mágica dice: {respuesta_oraculo}")
        print("-" * 50)

if __name__ == "__main__":
    iniciar_bola_magica()