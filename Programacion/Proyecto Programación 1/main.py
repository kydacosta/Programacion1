import tkinter as tk
from tkinter import messagebox
from catalogo import cargar_catalogo, guardar_catalogo
import paginas as paginas_mod
from colorama import Fore, Style, init
init(autoreset=True)

COLOR_BARRA_SUPERIOR = "#141414"
COLOR_MENU_LATERAL = "#181818"
COLOR_PANEL_PRINCIPAL = "#F5F5F5"
COLOR_HOVER = "#0099CC"

def bind_hover(button):
    button.bind("<Enter>", lambda e: button.config(bg=COLOR_HOVER))
    button.bind("<Leave>", lambda e: button.config(bg=COLOR_MENU_LATERAL))

def main():
    print(Fore.CYAN + "Iniciando programa..." + Style.RESET_ALL)

    catalogo = cargar_catalogo()

    print(Fore.GREEN + "Catálogo cargado correctamente." + Style.RESET_ALL)

    root = tk.Tk()
    root.title("🎮 GameStock Pro")
    root.geometry("1340x730")
    root.configure(bg=COLOR_PANEL_PRINCIPAL)

    barra_superior = tk.Frame(root, height=50, bg=COLOR_BARRA_SUPERIOR)
    barra_superior.pack(side="top", fill="x")

    titulo = tk.Label(barra_superior, text="🎮 GameStock Pro",
                      bg=COLOR_BARRA_SUPERIOR, fg="white", font=("Segoe UI", 16))
    titulo.pack(side="left", padx=20)

    btn_toggle_menu = tk.Button(
        barra_superior, text="≡", bg=COLOR_BARRA_SUPERIOR, fg="white",
        bd=0, font=("Segoe UI", 18)
    )
    btn_toggle_menu.pack(side="left", padx=10)

    menu_lateral = tk.Frame(root, width=220, bg=COLOR_MENU_LATERAL)
    menu_lateral.pack(side="left", fill="y")

    perfil = tk.Label(menu_lateral, text="Perfil", bg=COLOR_MENU_LATERAL,
                      fg="white", font=("Segoe UI", 20))
    perfil.pack(pady=18)

    panel_principal = tk.Frame(root, bg=COLOR_PANEL_PRINCIPAL)
    panel_principal.pack(side="right", expand=True, fill="both")

    def crear_boton(texto, comando):
        btn = tk.Button(
            menu_lateral, text=texto, bg=COLOR_MENU_LATERAL,
            fg="white", bd=0, anchor="w", font=("Segoe UI", 13),
            command=comando
        )
        btn.pack(fill="x", padx=10, pady=6)
        bind_hover(btn)
        return btn

    #Secciones laterales
    crear_boton("Inicio", lambda: paginas_mod.pagina_inicio(panel_principal, catalogo))
    crear_boton("Tabla", lambda: paginas_mod.pagina_tabla(panel_principal, catalogo))
    crear_boton("Grafica", lambda: paginas_mod.pagina_grafica(panel_principal, catalogo))
    crear_boton("Agregar", lambda: paginas_mod.abrir_form_agregar(panel_principal, catalogo))
    crear_boton("Buscar", lambda: paginas_mod.abrir_buscar(panel_principal, catalogo))

    crear_boton("Guardar", lambda: (
        guardar_catalogo(catalogo),
        print(Fore.BLUE + "Archivo guardado correctamente." + Style.RESET_ALL)
    ))

    crear_boton("Salir", root.destroy)

    def toggle_menu():
        if menu_lateral.winfo_ismapped():
            menu_lateral.pack_forget()
        else:
            menu_lateral.pack(side="left", fill="y")
    btn_toggle_menu.config(command=toggle_menu)

    paginas_mod.pagina_inicio(panel_principal, catalogo)

    def on_closing():

        print(Fore.YELLOW + "Intentando salir del programa..." + Style.RESET_ALL)

        if messagebox.askyesno("Salir", "¿Desea guardar los cambios antes de salir?"):
            try:
                guardar_catalogo(catalogo)
                print(Fore.BLUE + "Cambios guardados antes de salir." + Style.RESET_ALL)
            except Exception:
                print(Fore.RED + "Error al guardar antes de salir." + Style.RESET_ALL)

        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()

#“if __name__ == "__main__": es una condición especial que Python
#usa para identificar si un archivo se está ejecutando por sí mismo. Si es así, se ejecuta main(). 
#Si el archivo es importado por otro módulo, ese bloque no se ejecuta. Esto evita que el programa 
#arranque accidentalmente cuando se usan sus funciones desde otro archivo.”