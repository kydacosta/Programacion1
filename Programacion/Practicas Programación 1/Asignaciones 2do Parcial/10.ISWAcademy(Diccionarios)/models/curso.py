#GAJ278080

def agregar_curso():
    nombre = input("Nombre del curso:").strip().title()
    instructor = input("Instructor:").strip().title()
    aula = input("Aula asignada:").strip().upper()

    nuevo_curso = {
        "Nombre": nombre,
        "Instructor": instructor,
        "Aula": aula,
        "Alumnos": {}
    }
    return nuevo_curso

def buscar_curso_por_nombre(cursos, nombre_curso):
    nombre_buscado = nombre_curso.title()
    for curso_data in cursos:
        if curso_data["Nombre"] == nombre_buscado:
            return curso_data
        return None
    
    def eliminar_curso(cursos, nombre_curso):
        nombre_a_eliminar = nombre_curso.title()
        for i, curso_data in enumerate(cursos):
            if curso_data["Nombre"] == nombre_a_eliminar:
                cursos.pop(i)
                return f"¡Listo! Curso {nombre_a_eliminar} eliminado."
            return f"Ups, el curso {nombre_a_eliminar} no existe."
        
        def modificar_propiedad(cursos, nombre_curso, propiedad, nuevo_valor):
            curso_encontrado = buscar_curso_por_nombre(cursos, nombre_curso)

            if curso_encontrado:
                propiedad = propiedad.title()
                if propiedad in ["Instructor", "Aula"]:
                    curso_encontrado[propiedad] = nuevo_valor
                    return f"¡Genial! {propiedad} de {nombre_curso.title()} es ahora {nuevo_valor}"
                else:
                    return "Solo puedes cambiar el Instructor o el Aula."
                return f"No encontré el curso {nombre_curso.title()}."