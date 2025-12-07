#GAJ278080
def obtener_info_tienda():
    info_tienda = ("¡Game Over al aburrimiento!", 2020)
    return info_tienda

def crear_inventario():
    inventario_juegos = {
        "Cyberpunk 2077": {
            "precio": 59.99,
            "stock": 15
        },
        "Halo Reach": {
            "precio": 49.99,
            "stock": 20
        },
        "Resident Evil 4": {
            "precio": 39.99,
            "stock": 30
        }
    }
    return inventario_juegos

def mostrar_precio_segundo_juego(inventario):
    juego = "Halo Reach"
    precio = inventario[juego]["precio"]
    print(f"3. El precio de '{juego}' es: ${precio}")

def actualizar_stock(inventario, nombre_juego, cantidad):
    if nombre_juego in inventario and inventario[nombre_juego]["stock"] >= cantidad:
        inventario[nombre_juego]["stock"] -= cantidad
        return f"Venta realizada. Stock de '{nombre_juego}' actualizado. Nuevo stock: {inventario[nombre_juego]['stock']}"
    elif nombre_juego in inventario:
        return f"No hay suficiente stock de '{nombre_juego}'."
    else:
        return f"Juego '{nombre_juego}' no encontrado en el inventario."

def iniciar_tienda_desafio():
    
    info = obtener_info_tienda()
    stock = crear_inventario()
    
    primer_juego_key = "Cyberpunk 2077"
    
    print("--- INICIO DEL DESAFÍO ---")
    print(f"Información de la Tienda (Tupla): {info}")
    print("\nInventario Inicial:")
    print(stock)
    print("-" * 35)

    mostrar_precio_segundo_juego(stock)

    resultado_venta = actualizar_stock(stock, primer_juego_key, 1)
    print(f"4. {resultado_venta}")
    
    print("\n--- TAREAS COMPLETADAS ---")
    print("Inventario Final:")
    print(stock)

if __name__ == "__main__":
    iniciar_tienda_desafio()
