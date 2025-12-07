import curso
import alumno

cursos = []

def inicializar_datos():
    curso_ejemplo = {
        "Nombre": "Programacion I",
        "Instructor": "Ing. Jorge",
        "Aula": "B-201",  
        "Alumnos": {
            "278080": {"Nombre": "Jesus Acosta", "Carrera": "ING. Software"},
        }  
    }
    cursos.append(curso_ejemplo)

def mostrar_listado_y_detalle(nombre_curso=None):
    if not cursos:
        print("\n¡Ups! No hay cursos registrados todavía.")
        return
        
    if nombre_curso:
        curso_data = curso.buscar_curso_por_nombre(cursos, nombre_curso)
        if not curso_data:
            print(f"No se encontró el curso '{nombre_curso.title()}'.")
            return
            
        alumnos_dict = curso_data["Alumnos"]
        alumnos_count = len(alumnos_dict)

        print("\n--- DETALLE COMPLETO DEL CURSO ---")
        print(f"Curso: {curso_data['Nombre']}")
        print(f"Instructor: {curso_data['Instructor']}, Aula: {curso_data['Aula']}")
        print(f"Total de Alumnos Inscritos: {alumnos_count}")
        print("-------------------------------------------------")

        if alumnos_count > 0:
            print("LISTA DE ALUMNOS (ID | Nombre | Carrera):")
            for id_alum, datos_alum in alumnos_dict.items():
                print(f" -> {id_alum} | {datos_alum['Nombre']} | {datos_alum['Carrera']}")
        else:
            print("LISTA DE ALUMNOS: Vacía.")
        print("-------------------------------------------------")
        return
    
    print("\n--- LISTA GENERAL DE CURSOS (Conteo) ---")
    for c in cursos:
        conteo = len(c['Alumnos'])
        print(f"- {c['Nombre']} (Instructor: {c['Instructor']}) -> {conteo} Alumnos")
    print("------------------------------------------------")


def mostrar_menu():
    print("\n" + "-" * 30)
    print(" ISW Academy: Menú Principal ")
    print("-" * 30)

    print("1. AGREGAR Nuevo Curso.")
    print("2. ELIMINAR Curso.")
    print("3. MODIFICAR Instructor o Aula.")
    print("4. DAR ALTA Alumno.")
    print("5. DAR BAJA Alumno.")
    print("6. MOSTRAR LISTADO Y Conteo de Cursos.")
    print("Salir. ¡Cerrar el sistema!")
    print("-" * 30)


def iniciar_sistema():
    print("\nBienvenido a la ISW Academy.")
    inicializar_datos()
    print("Datos de prueba cargados.")

    while True:
        mostrar_menu()
        opcion = input("Elige tu opción (1-6 o Salir):").strip().lower()

        if opcion == "salir":
            print("Gracias por usar el sistema.")
            break
            
        elif opcion == "1":
            nuevoCurso = curso.agregar_curso()
            cursos.append(nuevoCurso)
            print(f"Curso {nuevoCurso['Nombre']} agregado con éxito.")

        elif opcion == "2":
            nombre = input("¿Qué curso quieres eliminar?:").strip().title()
            print(curso.eliminar_curso(cursos, nombre))

        elif opcion == "3":
            nombre = input("Curso a modificar: ").strip().title()
            propiedad = input("¿Modificar (I)nstructor o (A)ula?: ").strip().title()
            propiedad_key = "Instructor" if propiedad == "I" else "Aula" if propiedad == "A" else None

            if propiedad_key:
                nuevo_valor = input(f"Nuevo valor para {propiedad_key}: ").strip().title()
                print(curso.modificar_propiedad(cursos, nombre, propiedad_key, nuevo_valor))
            else:
                print("Opción de propiedad no válida.")

        elif opcion == "4":
            nombre_curso = input("Curso para dar de alta: ").strip().title()
            id_alumno = input("ID del alumno (clave): ").strip().upper()
            nombre_alumno = input("Nombre completo: ").strip().title()
            carrera = input("Carrera: ").strip().upper()
            print(alumno.dar_alta_alumno(cursos, nombre_curso, id_alumno, nombre_alumno, carrera))

        elif opcion == "5":
            nombre_curso = input("Curso para dar de baja: ").strip().title()
            id_alumno = input("ID del alumno a dar de baja: ").strip().upper()
            print(alumno.dar_baja_alumno(cursos, nombre_curso, id_alumno))
        
        elif opcion == "6":
            nombre = input("¿De qué curso quieres ver el detalle? (Deja vacío para ver el listado general): ").strip().title()
            mostrar_listado_y_detalle(nombre if nombre else None)

        else:
            print("Opción no válda. Prueba con 1-6 o 'Salir'.")

if __name__ == "__main__":
    iniciar_sistema()