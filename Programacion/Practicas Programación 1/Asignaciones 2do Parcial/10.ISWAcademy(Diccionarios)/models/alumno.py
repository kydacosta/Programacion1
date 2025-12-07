#GAJ27808

import curso

def crear_estructura_alumno(nombre_alumno, carrera):
    nuevo_alumno = {
        "Nombre": nombre_alumno.title(),
        "Carrera": carrera.upper()
    }
    return nuevo_alumno

def dar_alta_alumno(cursos, nombre_curso, id_alumno, nombre_alumno, carrera):
    curso_encontrado = curso.buscar_curso_por_nombre(cursos, nombre_curso)
    id_alumno = id_alumno.upper()

    if not curso_encontrado:
        return f"El Curso {nombre_curso.title()} no existe."
    
    alumnos = curso_encontrado["Alumnos"]

    if id_alumno in alumnos:
        return f"Ojo El ID {id_alumno} ya está registrado en este curso."
    
    nuevo_alumno = crear_estructura_alumno(nombre_alumno, carrera)
    alumnos[id_alumno] = nuevo_alumno
    return f"¡Bienvenido! {nombre_alumno.title()} con ID {id_alumno} dado de alta."

def dar_baja_alumno(cursos, nombre_curso, id_alumno):
    curso_encontrado = curso.buscar_curso_por_nombre(cursos, nombre_curso)
    id_alumno = id_alumno.upper()

    if not curso_encontrado:
        return f"El curso {nombre_curso.title()} no existe."
    
    alumnos = curso_encontrado["Alumnos"]

    if id_alumno not in alumnos:
        return f"Error: El ID {id_alumno} no está inscrito en este curso."
    
    nombre_baja = alumnos[id_alumno]["Nombre"]
    del alumnos[id_alumno]
    return f"{nombre_baja} con ID {id_alumno} dado de baja."