import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Fuente 1: Ventas internas
sales_data = {
    "GameID": ["G1","G2","G3","G4","G5","G6"],
    "Title": ["Cyber-Punk 2078", "Elder Scrolls V1"
              ,"Llama Tycoon", "Super Mario Odyssey2"
              ,"FIFA 2026", "Dark Souls VI"],
    "Genre": ["RPG","Simulation", "Platform"
              ,"Sports", "MMORPG"],
    "Publisher": ["Dev-Studios", "Bethesda", "Llama-Soft"
                  ,"Nintendo", "EA", "FromSoft"],
    "Units_Sold_Millions":[15.5,20.1,8.0,12.3,18.2,19.6]
}

sales_df = pd.DataFrame(sales_data)

#Fuente2: Reseñas de críticos (externo)
reviews_data = {
    "GameID": ["G1","G2","G3","G4","G5","G7"], #Nota. G5 falta, G7 Sobra
    "Critic_Score":[7.5,9.5,8.8,9.7,6.1,8.0], #Puntuación de 0 a 10
    "User_Score": [5.1,9.1,8.5,9.2,np.nan,7.5] #Un Nan! Alguien olvido puntuar FIFA
}

reviews_df = pd.DataFrame(reviews_data)

print("--- Datos de Ventas ---")
print(sales_df)
print("--- Datos de Ventas ---")
print (reviews_df)

# Limpieza de datos y preparación
#Desicion: Rellenaremos el User_Score que falta con el promedio (FIFA)
mean_user_score = reviews_df["User_Score"].mean()#Promedio de calificaciones de usuario
reviews_df["User_Score"] = reviews_df["User_Score"].fillna(mean_user_score)

print(f"\n--- Reseñas (Limpias, Nan rellenado con {mean_user_score})---")
print(reviews_df)

#Fusion de tablas (merge)
#Fusionar tabla de ventas con reseñas, GameID como llave
#INNER JOIN. nos quedamos con los juegos que existen en ambas tablas
#G6 va a desaoarecer, G7 Desaparecer
df = pd.merge(sales_df,reviews_df, on="Game_ID", how="inner")

print("\n--- Tabla fusionada de ventas+reseñas ---")
print(df)

#Crear nuevas columnas que nos den más información
#Columna Estimación de ingresos (asumiendo que valen $50 cada juego)
df["Revenue_Estimate_Billions"] = (df["Units_Sold_Millions"]*50)/1000

#Columna Brecha que hay entre reseñas criticos y la de los usuarios
df["Score_Gap"] = df["Critic_Score"]-df["User_Score"]

#Columna Estandar de Puntuación de los criticos (a 100)
df["Critic_Score_100"] = df["Critic_Score"] * 10

print("\n--- Tabla transformada (Con nuevas Columnas)")
print(df)