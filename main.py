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

   

@app.get('/UserForGenre/{genre}')
async def UserForGenre(genre: str):
    return {"Usuario con más horas jugadas para Género {genre}" : "us213ndjss09sdf",
            "Horas jugadas":[{"Año": 2013, "Horas": 203}, 
                             {"Año": 2012, "Horas": 100}, 
                             {"Año": 2011, "Horas": 23}]}


@app.get('/UsersRecommend/{anio}')
async def UsersRecommend(anio: str):
    if anio.isdigit() == True:
        anio = int(anio)
        return  [{"Puesto 1" : "Juego 1"}, {"Puesto 2" : "Juego 2"},{"Puesto 3" : "Juego 3"}]


@app.get('/UsersNotRecommend/{anio}')
async def UsersNotRecommend(anio: str):
    if anio.isdigit() == True:
        anio = int(anio)
        return  [{"Puesto 1" : "Juego 1"}, {"Puesto 2" : "Juego 2"},{"Puesto 3" : "Juego 3"}]
    
@app.get('/sentiment_analysis/{anio}')
async def sentiment_analysis(anio: str):
    if anio.isdigit() == True:
        anio = int(anio)
        return   {'Negative':182, 'Neutral': 120, 'Positive': 278}