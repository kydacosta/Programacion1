#GAJ27808
def agregar_curso():
    nombre = input("Nombre del curso: ").strip().title()
    aula = input("Nombre del aula: ").strip().upper()
    instructor = input("Nombre del instructor: ").strip().title()
    
    curso = {
        "Nombre": nombre,
        "Aula": aula,
        "Instructor": instructor,
        "Alumnos": []
    }
    return curso

def eliminar_curso(cursos, id_curso):
    if 0 <= id_curso < len(cursos):
        return f"Curso '{cursos.pop(id_curso)['Nombre']}' eliminado."
    return "ID de curso no válido."
    
def modificar_propiedad(curso, propiedad, nuevo_valor):
    propiedad = propiedad.title()
    if propiedad in ["Nombre", "Aula", "Instructor"]:
        curso[propiedad] = nuevo_valor
        return f"{propiedad} actualizado a '{nuevo_valor}'."
    return "Propiedad no válida."

def dar_baja_alumno(alumnos, id_alumno):
    if 0 <= id_alumno < len(alumnos):
        return f"Alumno '{alumnos.pop(id_alumno)}' dado de baja."
    return "ID de alumno no válido."

def buscar_curso_por_id(cursos, id_curso):
    if 0 <= id_curso < len(cursos):
        return cursos[id_curso]
    return None

def mostrar_alumnos(curso):
    print(f"\n==== Alumnos en ({curso['Nombre']}) ====")
    if not curso["Alumnos"]:
        print("No hay alumnos inscritos.")
        return
        
    for i, alumno_nombre in enumerate(curso["Alumnos"]):
        print(f"ID:{i} - {alumno_nombre}")

def mostrar_cursos(cursos):
    print("\n--- LISTADO DE CURSOS ---")
    if not cursos:
        print("No hay cursos registrados.")
        return
        
    for i, curso_data in enumerate(cursos):
        print(f"ID:{i} - {curso_data['Nombre']} (Aula: {curso_data['Aula']})")

def revisar_alumnos(cursos):
    print("\n--- REVISIÓN GENERAL ---")
    if not cursos:
        print("No hay cursos.")
        return
        
    for curso_data in cursos:
        num_alumnos = len(curso_data["Alumnos"])
        print(f"Curso: {curso_data['Nombre']} (Instructor: {curso_data['Instructor']})")
        print(f"  Total: {num_alumnos}. Lista: {', '.join(curso_data['Alumnos'])}")

def iniciar_sistema():
    cursos = []
    
    while True:
        op2 = input("""
                \n--- MENÚ DE GESTIÓN ---
                1. Agregar curso        | 5. Dar baja alumno
                2. Eliminar curso       | 6. Mostrar lista alumnos
                3. Modificar propiedad  | 7. Mostrar cursos
                4. Agregar alumno       | 8. Revisión general
                9. Salir
                Selecciona una opción: """).strip()
        
        if op2 == '9':
            print("Saliendo del sistema.")
            break
        
        if not op2.isdigit():
            print("Opción no válida. Ingresa un número.")
            continue
            
        opcion = int(op2)
        
        try:
            if opcion == 1:
                cursos.append(agregar_curso())
                print("Curso agregado.")
            
            elif opcion == 2:
                mostrar_cursos(cursos)
                idCurso = int(input("ID del curso a eliminar: "))
                print(eliminar_curso(cursos, idCurso))

            elif opcion == 3:
                mostrar_cursos(cursos)
                idCurso = int(input("ID del curso a modificar: "))
                curso_a_modificar = buscar_curso_por_id(cursos, idCurso)
                if curso_a_modificar:
                    propiedad = input("¿Modificar Nombre, Aula o Instructor?: ").strip()
                    nuevo_valor = input(f"Nuevo valor para {propiedad}: ").strip().title()
                    print(modificar_propiedad(curso_a_modificar, propiedad, nuevo_valor))
                else:
                    print("ID de curso no válido.")

            elif opcion == 4:
                mostrar_cursos(cursos)
                idCurso = int(input("ID del curso: "))
                curso_destino = buscar_curso_por_id(cursos, idCurso)
                if curso_destino:
                    alumno_nuevo = input("Nombre del alumno: ").strip().title()
                    curso_destino["Alumnos"].append(alumno_nuevo)
                    print(f"Alumno '{alumno_nuevo}' agregado.")
                else:
                    print("ID de curso no válido.")
            
            elif opcion == 5:
                mostrar_cursos(cursos)
                idCurso = int(input("ID del curso: "))
                curso_destino = buscar_curso_por_id(cursos, idCurso)
                if curso_destino:
                    mostrar_alumnos(curso_destino)
                    idAlumno = int(input("ID del alumno a dar de baja: "))
                    print(dar_baja_alumno(curso_destino["Alumnos"], idAlumno))
                else:
                    print("ID de curso no válido.")

            elif opcion == 6:
                mostrar_cursos(cursos)
                idCurso = int(input("ID del curso para ver alumnos: "))
                curso_destino = buscar_curso_por_id(cursos, idCurso)
                if curso_destino:
                    mostrar_alumnos(curso_destino)
                else:
                    print("ID de curso no válido.")

            elif opcion == 7:
                mostrar_cursos(cursos)

            elif opcion == 8:
                revisar_alumnos(cursos)

            else:
                print("Opción no reconocida.")
                
        except ValueError:
            print("Error: Ingresa un ID numérico válido.")

if __name__ == "__main__":
    iniciar_sistema()
