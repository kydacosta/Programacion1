def obtener_juego(catalogo, nombre_buscar):
    nombre = nombre_buscar.strip().lower()
    for juego in catalogo:
        if juego.get("nombre", "").strip().lower() == nombre:
            return juego
    return None

def agregar_juego(catalogo, data):
    nombre = data.get("nombre", "").strip().title()
    if not nombre:
        return False, "El nombre no puede estar vacío."
    if obtener_juego(catalogo, nombre):
        return False, f"El juego '{nombre}' ya existe."

    try:
        precio = float(data.get("precio", 0))
        inventario = int(data.get("inventario", 0))
        if precio < 0 or inventario < 0:
            return False, "Precio o inventario no pueden ser negativos."
    except Exception:
        return False, "Formato inválido para precio o inventario."

    nuevo = {
        "nombre": nombre,
        "precio": precio,
        "inventario": inventario,
        "categoria": data.get("categoria", "").strip().title(),
        "plataformas": data.get("plataformas", "").strip().title(),
        "descripcion": data.get("descripcion", "").strip()
    }
    catalogo.append(nuevo)
    return True, f"Juego '{nombre}' agregado correctamente."

def eliminar_juego(catalogo, nombre):
    juego = obtener_juego(catalogo, nombre)
    if juego:
        catalogo.remove(juego)
        return True, f"Juego '{nombre}' eliminado."
    return False, "No se encontró el juego."

def buscar_juegos(catalogo, termino):
    termino = termino.strip().lower()
    resultados = []
    for j in catalogo:
        if termino in j.get("nombre", "").lower() or termino in j.get("categoria", "").lower():
            resultados.append(j)
    return resultados
