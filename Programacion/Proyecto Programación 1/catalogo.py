import pandas as pd
import os

ARCHIVO_DATOS = "catalogo_juegos.csv"
COLUMNAS = ["nombre", "precio", "inventario", "categoria", "plataformas", "descripcion"]

CATEGORIAS = (
    "Acción",
    "Aventura",
    "RPG",
    "Shooter",
    "Deportes",
    "Carreras"
)

PLATAFORMAS = (
    "Nintendo Switch",
    "PS4",
    "PS5",
    "Xbox One",
    "Xbox Series",
    "PC"
)

def cargar_catalogo():
    if os.path.exists(ARCHIVO_DATOS):
        df = pd.read_csv(ARCHIVO_DATOS)
        for col in COLUMNAS:
            if col not in df.columns:
                df[col] = ""
        return df[COLUMNAS].to_dict("records")

    #Catálogo inicial
    inicial = [
        {
            "nombre": "The Legend of Zelda: Tears of the Kingdom",
            "precio": 90.0, "inventario": 250,
            "categoria": "Acción / Aventura", "plataformas": "Nintendo Switch",
            "descripcion": "Secuela destacada de la saga Zelda."
        },
        {
            "nombre": "God of War Ragnarök",
            "precio": 60.0, "inventario": 400,
            "categoria": "Acción / Hack and Slash", "plataformas": "PS4 / PS5",
            "descripcion": "Continuación del reinicio de God of War 2018."
        },
        {
            "nombre": "Halo Infinite",
            "precio": 30.0, "inventario": 200,
            "categoria": "Shooter", "plataformas": "Xbox Series / One",
            "descripcion": "Shooter de ciencia ficción."
        }
    ]
    return inicial

def guardar_catalogo(catalogo, ruta=None):
    ruta = ruta if ruta else ARCHIVO_DATOS
    df = pd.DataFrame(catalogo)

    for col in COLUMNAS:
        if col not in df.columns:
            df[col] = ""

    df = df[COLUMNAS]
    df.to_csv(ruta, index=False)
