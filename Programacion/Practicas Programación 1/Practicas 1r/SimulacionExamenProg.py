#Examen de Programacion I - Simulacion en Python 

#Lista de preguntas: [Pregunta, [Opcion A, B, C, D], Indice de la respuesta correcta (0=A, 1=B, 2=C, 3=D)]

examen = [
    [
        "1. ¿Que estructura de control es mas adecuada para iterar sobre una secuencia de elementos un numero de veces conocido de antemano?",
        ["A) Bucle 'para'", "B) Sentencia condicional 'Si'", "C) Bucle 'repetir'", "D) Bucle 'mientras'" ],
        0
    ],
    [
    "2. ¿Que es un algoritmo?",
    ["A) Un conjunto de instrucciones escritas en codigo binario.", "B) un lenguaje de programacion especifico.", "C) El codigo fuente de un programa de computadora.", "D) Una secuencia de pasos finitos y bien definidos para resolver un problema"],
    3
    ],
    [
    "3. El lenguaje maquina esta compuesto por:",
    ["A) Simbolos logicos y matematicos", "B) Pseudocodigo", "C) Instrucciones en ingles abreviado", "D) Codigo binario"],
    3
    ],
    [
    "4. ¿Cual de los siguientes componentes NO es parte fundamental de la arquitectura de Von Neumann?",
    ["A) Sistema de entrada/salida", "B) CPU", "C) Tarjeta Grafica", "D) Memoria principal"],
    2
    ],
    [
    "5. Un lenguaje de programacion de alto nivel se caracteriza por:",
    ["A) Ser muy dificil de aprender y leer.", "B) Ser el mas rapido en tiempo de ejecucion.", "C) Tener el control directo y preciso sobre el hardware.", "D) Ser independiente de la arquitectura de la computadora."],
    3
    ],
    [
    "6. El lenguaje Java e considerado un lenguaje de nivel...",
    ["A) Bajo", "B) Muy alto", "C) Medio", "D) Alto"],
    3
    ],
    [
    "7. Un programa de computadora es esencialemente:",
    ["A) Una coleccion de algoritmos.", "B) El sistema operativo de la computadora.", "C) Un dispositivo de hardware", "D) Una secuencia de instrucciones que la computadora ejecuta",],
    3
    ],
    [
    "8. En pseudocodigo ¿Que estructura de control se utiliza para ejecutar un bloque de codigo solo si se cumple una condicion especifica?",
    ["A) Condicional o de seleccion", "B) Repetitiva 'para'", "C) Secuencial", "D) Repetitiva 'para'"],
    0
    ],
    [
    "9. El proposito principal del pseudocodigo es:",
    ["A) El traducir automaticamente codigo de alto nivel a lenguaje maquina.", "B) Ejecutar programas de manera mas eficiente que un lenguaje compilado", "C) Planificar y escribir la logica de un algoritmo de forma legible para los humanos", "D) Proporcionar un control directo sobre los registros del procesador"],
    2
    ],
    [
    "10. ¿Cual es la principal diferencia entre el bucle 'mientras' (while) y un bucle 'repetir' (do-while)",
    ["A) El bucle 'mientras' puede no ejecutarse, mientras que el 'repetir' se ejecuta al menos una vez.", "B) No hay ninguna diferencia, son intercambiables.", "C) El bucle 'mientras' es mas rapido que el repetir", "D) El bucle 'repetir' solo usa numeros, mientras que el 'mientras' puede usar cualquier condicion."],
    0
    ],
]


#Contador  de respuestas
respuestasC = 0
totalP = len(examen)

print ("----------------------------------------------------")
print ("     INICIO DE EXAMEN       ")
print ("----------------------------------------------------")
print ("     Responda con la letra de opcion (A, B, C, D).")
print ("----------------------------------------------------")

for i in range (totalP):
    pregunta, opciones, indiceC = examen[i]

    print (f"Pregunta {i + 1}: {pregunta}")
    for opcion in opciones:
        print (f"        {opcion}")

#Bucle para asegurar entrada valida (esto lo saque de IA, ya que me quede atorado)
while True:
    respuestaU = input ("Tu respuesta (A/B/C/D): ").upper()

    if respuestaU in ('A', 'B', 'C', 'D'):
        break 
    else:
        print ("Entrada Invdalida." \
        "Ingresa A, B, C, D.")


#Uso del if, elif, else para convertir las letras en los numeros de respuesta

if respuestaU == 'A':
    indiceU = 0
elif respuestaU == 'B':
    indiceU = 1
elif respuestaU == 'C':
    indiceU = 2
else:
    indiceU = 3

#Comprobar respuestas

if indiceU == indiceC:
    respuestasC += 1
    print ("Correcto!")
else: 
    opcionCL = chr(ord('A') + indiceC)
print (f"Incorrecto. La respuesta correcta era la opcion {opcionCL}")

calificacion = (respuestasC / totalP) * 100

print ("----------------------------------------------------")
print ("        FIN DEL EXAMEN           ")
print ("----------------------------------------------------")
print (f"Resultado: {respuestasC} de {totalP} respuestas correctas.")
print (f"Calificacion: {int(calificacion)}/100.")

if int (calificacion) >= 50:
    print ("Aprobaste!")
else:
    print ("Sigue estudiando burro!")

print ("----------------------------------------------------")
