import tkinter as tk
from tkinter import ttk, messagebox
from operaciones import obtener_juego, agregar_juego, buscar_juegos
from catalogo import guardar_catalogo
from grafica import crear_grafica


#Inicio
def pagina_inicio(panel, catalogo):
    for w in panel.winfo_children():
        w.destroy()

    frame = tk.Frame(panel, bg="white")
    frame.pack(fill="both", expand=True)

    titulo = tk.Label(frame, text="Programa de Inventario de Videojuegos",
                      font=("Segoe UI", 22), bg="white")
    titulo.pack(pady=20)

    texto = tk.Label(
        frame,
        text=(
            "  Inventario de VideoJuegos\n"

            "\n- Gestión de inventario\n"
            "- Agregar videojuegos\n"
            "- Modificar videojuegos\n"
            "- Buscar por nombre o categoría\n"
            "- Visualizar gráfica de inventario\n"
            "- Guardar cambios en archivo\n"

            "\n  Desarrolladores\n"
            "\n"
            "Jesus Abraham Ruis Armiento - 279158\n"
            "Jose Arturo Rometo Romero - 244315\n"
            "Luis Alejandro Verdugo - 281122\n"
            "Alexis Vicente Reyna Mejia - 281429\n"
            "Jesus Gonzalez Acosta - 278080\n"
        ),
        font=("Segoe UI", 14),
        bg="white"
    )
    texto.pack(pady=10)

    return frame


#Tabla
def pagina_tabla(panel, catalogo):
    for w in panel.winfo_children():
        w.destroy()

    frame = tk.Frame(panel, bg="white")
    frame.pack(fill="both", expand=True)

    contenedor_botones = tk.Frame(frame, bg="white")
    contenedor_botones.pack(fill="x", padx=10, pady=10)

    tabla = ttk.Treeview(frame, columns=["nombre", "precio", "inventario",
                                         "categoria", "plataformas", "descripcion"],
                         show="headings")
    tabla.pack(fill="both", expand=True, padx=10, pady=10)

    for col in tabla["columns"]:
        tabla.heading(col, text=col.title())
        tabla.column(col, width=150)

    for juego in catalogo:
        tabla.insert("", tk.END, values=list(juego.values()))

    #Botón AGREGAR
    btn_agregar = tk.Button(contenedor_botones, text="Agregar",
                            command=lambda: abrir_form_agregar(panel, catalogo))
    btn_agregar.pack(side="left", padx=5)

    #Botón MODIFICAR
    btn_modificar = tk.Button(
        contenedor_botones,
        text="Modificar Seleccionado",
        command=lambda: _modificar_desde_tabla(panel, tabla, catalogo)
    )
    btn_modificar.pack(side="left", padx=5)

    #Botón ELIMINAR
    btn_eliminar = tk.Button(
        contenedor_botones,
        text="Eliminar Seleccionado",
        command=lambda: _eliminar_desde_tabla(tabla, catalogo)
    )
    btn_eliminar.pack(side="left", padx=5)

    return frame

def _eliminar_desde_tabla(tabla, catalogo):
    seleccionado = tabla.selection()
    if not seleccionado:
        return

    valores = tabla.item(seleccionado, "values")
    nombre = valores[0]

    for j in catalogo:
        if j["nombre"] == nombre:
            catalogo.remove(j)
            break

    tabla.delete(seleccionado)
    guardar_catalogo(catalogo)

def _modificar_desde_tabla(panel, tabla, catalogo):
    seleccionado = tabla.selection()
    if not seleccionado:
        return

    valores = tabla.item(seleccionado, "values")
    nombre = valores[0]

    abrir_form_modificar(panel, catalogo, nombre)

#Agregar
def abrir_form_agregar(panel, catalogo):
    for w in panel.winfo_children():
        w.destroy()

    frame = tk.Frame(panel, bg="white")
    frame.pack(fill="both", expand=True)

    entradas = {}

    campos = ["nombre", "precio", "inventario", "categoria", "plataformas", "descripcion"]

    for i, campo in enumerate(campos):
        tk.Label(frame, text=campo.title(), bg="white").grid(row=i, column=0, padx=10, pady=10)
        entrada = tk.Entry(frame, width=40)
        entrada.grid(row=i, column=1, padx=10, pady=10)
        entradas[campo] = entrada

    def guardar():
        datos = {c: entradas[c].get() for c in entradas}
        ok, msg = agregar_juego(catalogo, datos)
        messagebox.showinfo("Mensaje", msg)
        if ok:
            guardar_catalogo(catalogo)

    tk.Button(frame, text="Guardar", command=guardar).grid(row=len(campos), column=0, pady=20)
    tk.Button(frame, text="Regresar",
              command=lambda: pagina_tabla(panel, catalogo)).grid(row=len(campos), column=1, pady=20)

#Modificar
def abrir_form_modificar(panel, catalogo, nombre_original):
    for w in panel.winfo_children():
        w.destroy()

    frame = tk.Frame(panel, bg="white")
    frame.pack(fill="both", expand=True)

    juego = obtener_juego(catalogo, nombre_original)
    if not juego:
        messagebox.showerror("Error", "No se encontró el juego.")
        return

    entradas = {}
    campos = ["nombre", "precio", "inventario", "categoria", "plataformas", "descripcion"]

    for i, campo in enumerate(campos):
        tk.Label(frame, text=campo.title(), bg="white").grid(row=i, column=0, padx=10, pady=10)
        entrada = tk.Entry(frame, width=40)
        entrada.insert(0, juego[campo])
        entrada.grid(row=i, column=1, padx=10, pady=10)
        entradas[campo] = entrada

    def guardar():
        for c in entradas:
            juego[c] = entradas[c].get()

        guardar_catalogo(catalogo)
        messagebox.showinfo("Modificado", "Cambios guardados.")
        pagina_tabla(panel, catalogo)

    tk.Button(frame, text="Guardar Cambios", command=guardar).grid(row=len(campos), column=0, pady=20)
    tk.Button(frame, text="Regresar",
              command=lambda: pagina_tabla(panel, catalogo)).grid(row=len(campos), column=1, pady=20)

# Buscar
def abrir_buscar(panel, catalogo):
    for w in panel.winfo_children():
        w.destroy()

    frame = tk.Frame(panel, bg="white")
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text="Buscar", font=("Segoe UI", 16), bg="white").pack(pady=10)

    entrada = tk.Entry(frame, width=40)
    entrada.pack(pady=10)

    tabla = ttk.Treeview(frame, columns=["nombre", "precio", "inventario",
                                         "categoria", "plataformas", "descripcion"],
                         show="headings")
    tabla.pack(fill="both", expand=True, padx=10, pady=10)

    for col in tabla["columns"]:
        tabla.heading(col, text=col.title())
        tabla.column(col, width=150)

    def buscar():
        for i in tabla.get_children():
            tabla.delete(i)

        resultados = buscar_juegos(catalogo, entrada.get())

        for r in resultados:
            tabla.insert("", tk.END, values=list(r.values()))

    tk.Button(frame, text="Buscar", command=buscar).pack(pady=10)

# Gráfica
def pagina_grafica(panel, catalogo):
    crear_grafica(panel, catalogo)

