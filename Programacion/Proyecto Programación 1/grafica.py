import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def crear_grafica(panel, catalogo):
    for w in panel.winfo_children():
        w.destroy()

    frame = tk.Frame(panel, bg="white")
    frame.pack(fill="both", expand=True)

    if not catalogo:
        tk.Label(frame, text="No hay datos para graficar.", bg="white").pack(pady=15)
        return

    nombres = [j["nombre"] for j in catalogo]
    inventarios = [int(j["inventario"]) for j in catalogo]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(nombres, inventarios)
    ax.set_xlabel("Videojuegos")
    ax.set_ylabel("Inventario")
    ax.set_title("Inventario de Videojuegos")
    plt.xticks(rotation=45, ha="right")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
