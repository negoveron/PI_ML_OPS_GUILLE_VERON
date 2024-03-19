import pandas as pd
from fastapi import FastAPI

app = FastAPI()



# Endpoints de la API
# @profile
@app.get('/PlayTimeGenre/{genre}')
async def PlayTimeGenre(genre: str):
    try:
        df_genero = pd.read_csv("data/play_time_genre.csv")

        # Filtrar el DataFrame por el género especificado

        df_genero = df_genero[df_genero["genre"] == genre.lower()]

        anio = list(df_genero[df_genero["playtime"] == df_genero["playtime"].max()]["anio"])[0]
        
        return {f"Año de lanzamiento con más horas jugadas para {genre}": anio}

    except Exception as e:
        return {"error": str(e)}     


