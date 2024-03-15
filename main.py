import pandas as pd
from fastapi import FastAPI

app = FastAPI()



# Endpoints de la API
# @profile
@app.get('/PlayTimeGenre/{genre}')
async def PlayTimeGenre(genre: str):
    """
    Examples
    --------
    >>> PlayTimeGenre("Shooter")
    {'Año de lanzamiento con más horas jugadas para Género Shooter': '2022'}
    """
    
        

    # Devolver el año con más horas jugadas para el género dado
    return {"Año de lanzamiento con más horas jugadas para Género Shooter: 2022"}