import tkinter as tk
#1. Creación de la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry ("320x500")

#2.Agregar los widgets
botones_texto = ("C", "/", "*", "-",
                 "7", "8", "9", "+",
                 "4", "5", "6", "",
                 "1", "2", "3", "=",
                 "0", ".", "", "")

historico = tk.Label(root
                     ,bg="#502929" 
                     ,font="Roboto 14"
                     ,width=15
                     ,bd=0
                     )
historico.pack(pady=5, padx=10, fill="x")


resultado = tk.Entry(root
                    ,bg="#F0F0F0"
                    ,bd=1
                    ,font="Roboto 24"
                    ,width=15
                    ,justify="right"
                    )

resultado.pack(padx=10, fill="x")

contenedor_botones = tk.Frame(root,bg="#F0F0F0")
contenedor_botones.pack(pady=5,padx=10,fill="both")

acumulador=0
for row in range(5):
    for column in range(4):
        boton = tk.Button(contenedor_botones
                          ,text=botones_texto[acumulador]
                          ,bg="#6ec3f5"
                          ,fg="#272727"
                          ,font="Roboto 20"
                          ,bd=0
                          ,width=4
                          ,height=1
                          )
        #Pintar lois botones de colores
        if botones_texto[acumulador]=="C":
            boton.config(bg="#FF4D4D")
        elif botones_texto[acumulador] in ("/", "*","-","+"):
            boton.config(bg="#005E83")
        if botones_texto[acumulador] != "":

            if botones_texto[acumulador] =="+":
                boton.config(height=3)
                boton.grid(row=row, column=column
                           , rowspan=2, padx=1, pady=5)
                
            elif botones_texto[acumulador] =="=":
                boton.config(height=3, bg="#E28E1F")
                boton.config(width=3)
                boton.grid(row=row, column=column
                           , rowspan=2, padx=1, pady=5)
                
            elif botones_texto[acumulador] =="0":
                boton.config(width=8)
                boton.grid(row=row, column=column
                           , rowspan=2, padx=1, pady=5)
            
            elif botones_texto[acumulador] ==".":
                boton.grid(row=row, column=column
                           , rowspan=2, padx=1, pady=5)
                
            else: boton.grid(row=row, column=column, padx=1, pady=1)
                
            boton.grid(row=row, column=column, padx=1, pady=5)
        acumulador+=1



root.mainloop()