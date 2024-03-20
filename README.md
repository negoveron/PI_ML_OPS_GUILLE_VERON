# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

El objetivo de este proyecto es emular un escenario real para poner en práctica los conocimientos adquiridos durante el bootcamp. Para ello se pretende idealizar una situación dentro de una empresa que maneja una plataforma de juegos. Se cuenta con información sobre los jugadores, sus interaciones y sus opininones.

## **Propuesta de trabajo**

**`Transformaciones`**:  Abarca la lectura, carga y transformación de los datos.

**`Feature Engineering`**:  Se debe crear la columna ***'sentiment_analysis'*** aplicando análisis de sentimiento con NLP.

**`Desarrollo API`**:   disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que se proponen son las siguientes:


+ def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.
  
+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

+ def **UsersNotRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

+ def **sentiment_analysis( *`año` : int* )**:
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento. 


**`Deployment`**: disponibilizar los datos en un servicio que permita ser consumida desde la web.

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_


**`Modelo de aprendizaje automático`**: 

Si es un sistema de recomendación item-item:
+ def **recomendacion_juego( *`id de producto`* )**:
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

Si es un sistema de recomendación user-item:
+ def **recomendacion_usuario( *`id de usuario`* )**:
    Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.


**`Video`**: explicativo de todo el proceso.
 
 
# Tabla de contenidos
1. [Cómo Ejecutar el Proyecto](#ejecutar)

4.  [Data Engineering](#dataengineer)
    1. [Repositorio y Conjuntos de Datos](#datos)
    2. [Preprocesamiento de Datos](#preprocesamiento)
5. [Análisis de Datos](#analisis)
    1. [Descripción del Proyecto](#descripcion)
6. [Funciones de la API](#funciones)
7. [Deployment y la API](#deploy)
8. [Archivos Generados](#archivos)
9. [Contribuciones y Colaboraciones](#contribuciones)
10. [Links](#links)
11. [Licencia](#licencia)
12. [Contacto](#contacto)
13. [Menciones y agradecimientos](#menciones)
------------------------------------------------------------------------------------------------------------------------------------
<a name="ejecutar"></a>

## Cómo Ejecutar el Proyecto 

Para ejecutar el proyecto localmente, se puede realizar de la siguiente manera:

1. Clonar el repositorio
2. Ejecutar los archivos en el siguiente orden: 1° el `ETL.ipynb`, 2° `EDA.ipynm` y finalmente el `main.py`

<a name="dataengineer"></a>

## Data Engineering

<a name="datos"></a>

### Repositorio y Conjuntos de Datos

- El repositorio del proyecto se encuentra disponible en [GitHub](https://github.com/soyHenry/PI_ML_OPS/tree/PT?tab=readme-ov-file).
- Los conjuntos de datos utilizados se encuentran disponibles en [Google Drive](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj).

<a name="preprocesamiento"></a>

### Preprocesamiento de Datos

- Se realiza la carga y limpieza de los conjuntos de datos utilizando Python y las siguientes librerías:
  - Pandas
  - NumPy
  - Matplotlib
  - NLTK

<a name="analisis"></a>

## Análisis de Datos

<a name="descripcion"></a>

### Descripción del Proyecto

El proyecto se divide en las siguientes secciones principales:

1. **Exploración de Datos:** Análisis inicial de los conjuntos de datos para comprender su estructura y características.
2. **Limpieza de Datos:** Proceso de limpieza y preprocesamiento de los datos para eliminar valores nulos, duplicados y realizar correcciones.
3. **Transformación de Datos:** Conversión de tipos de datos, extracción de información relevante y preparación de los datos para su análisis.
4. **Análisis de Sentimientos:** Utilización de análisis de sentimientos para evaluar las opiniones de los usuarios en las reseñas de juegos.
5. **Generación de Reportes:** Creación de visualizaciones y reportes estadísticos para identificar patrones y tendencias en los datos.

<a name="funciones"></a>

## Funciones de la API

El proyecto también incluye la implementación de una API para proporcionar acceso a datos procesados y funcionalidades específicas. Las principales funciones de la API incluyen:

1. **UserForGenre():** Devuelve el año con más horas jugadas para un género específico.
2. **UsersRecommend():** Proporciona información sobre los usuarios que recomiendan un juego.
3. **UsersNotRecommend():** Proporciona información sobre los usuarios que no recomiendan un juego.
4. **SentimentAnalysis():** Realiza análisis de sentimientos en las reseñas de los usuarios.

para más información se puede consultar la documentación de la api en :
Ingresar enlace de Render/Docs

<a name="deploy"></a>

## Deployment
La API puede ser probada en local utilizando uvicorn con el siguiente comando dentro de la carpeta raíz del proyecto:

```bash
uvicorn main:app --reload
```

la API está deployada en Render, cada modificación hecha en el archivo `main.py` se verá de forma automática en uvicor, pero debe ser actualizada manualmente en el Deploy de Render.

<a name="archivos"></a>

## Archivos Generados

El proyecto genera varios archivos CSV con datos preprocesados y resultados de análisis para su posterior uso y visualización.

- `PlayTimeGenre.csv`: Contiene información sobre el tiempo de juego por género y año.
- Otros archivos CSV generados para cada función de la API con los resultados correspondientes.

<a name="contribuciones"></a>

## Contribuciones y Colaboraciones

¡Las contribuciones al proyecto son bienvenidas! Si deseas colaborar, no dudes en enviar una solicitud de extracción (pull request) o abrir un problema (issue) en el repositorio de GitHub.

<a name="links"></a>

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://your.github.com/awesome-project/
- Repository: https://github.com/your/awesome-project/
- Issue tracker: https://github.com/your/awesome-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project: https://github.com/your/other-project/
  - Someone else's project: https://github.com/someones/awesome-project/

<a name="licencia"></a>

## Licencia

Este proyecto se distribuye bajo la [licencia MIT](https://choosealicense.com/licenses/mit/). Consulta el archivo `LICENSE.txt` para obtener más detalles.

<a name="contacto"></a>

## Contacto

Para obtener más información o realizar preguntas sobre el proyecto, puedes ponerte en contacto con el autor:

- Nombre: Misael García Torres
- Teléfono: +56 931 854 247
- Correo Electrónico: [misagtor@gmail.com)
- LinkedIn: [linkedin.com/in/mgarciat](https://www.linkedin.com/in/mgarciat/)

<a name="menciones"></a>

## Menciones y agradecimientos

Para la realización de este proyecto se utilizaron los conocimientos adquiridos en el Bootcamp de Data Science del Equipo de "[Henry](https://web.soyhenry.com/about-us)", agradezco también a mis TAs Roberto y Rafa, quienes me acompañaron durante todo el proceso, son unos cracks.
