
![images](https://github.com/user-attachments/assets/2c559b96-5d09-48dd-b395-111783fee614)


# Proyecto integrador 1 Steam:

 En este repositorio se podra visualizar el primer proyecto integrador del Bootcamp Henry para Data Science.



## Objetivo


### Situándonos en el rol de Data Scientist, desarrollaremos un Sistema de Recomendación para la plataforma de videojuegos online Steam Games. 

 El MVP debe desplegarse como una API que pueda ser consumida desde la Web.



## Fuentes de Datos

### Para comenzar los datos provistos fueron 3 archivos JSON que se pueden encontrar en el siguiente [link](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

- australian_user_reviews.json': en este archivo se encuentran los comentarios (reviews) de los usuarios de Australia a los juegos de la plataforma. Además de la review, hay una columna 'recommend' que toma valor 'True' en caso de que el usuario recomiende el juego, y 'False' en caso contrario.

  
- 'australian_users_items': en este archivo se encuentran todos los usuarios de Australia, y para cada usuario detalles sobre los juegos comprados (como tiempo de juego).

  
- 'output_steam_games': aquí se encuentran los detalles de los juegos de steam, como género, tags, especificaciones.
![Screenshot_4](https://github.com/user-attachments/assets/cdb03c4a-6431-43ef-945b-9ba9910a3038)
![Screenshot_5](https://github.com/user-attachments/assets/25a57250-c3af-4cea-b341-d95bc8906e5e)


## ETL


El proceso de **Extracción, Transformación y Carga (ETL)** fue desarrollado en tres **Jupyter notebooks** por separado, donde se realizó la **limpieza de los datos**, incluyendo:

- Eliminación de duplicados
- Eliminación de filas vacías
- Tratamiento de valores nulos

Puedes encontrarlos [aquí](https://github.com/Santino-Rocchietti/P1-Steam/tree/main/ETL)


En cada uno de los archivos encontrarás el código comentado, lo que permitirá entender las modificaciones realizadas durante el proceso. Los datos resultantes fueron exportados en formato **Parquet** y los puedes encontrar en este [enlace](https://github.com/Santino-Rocchietti/P1-Steam/tree/main/Clean%20Data)


## EDA

Luego de realizada la **limpieza de los datos**, se llevó a cabo un [**Análisis Exploratorio de Datos (EDA)**](https://github.com/Santino-Rocchietti/P1-Steam/blob/main/EDA_steam.ipynb). El objetivo del análisis es entender las relaciones entre los diferentes datos, encontrar insights que permitan mejorar la interpretación de los mismos y retroalimentar el desarrollo del modelo con nuevas perspectivas.

En el notebook encontrarás visualizaciones que muestran información interesante, como:

- Qué géneros de juegos son los más consumidos
- Cuáles son los juegos más caros
- Qué palabras son las más frecuentes en los títulos

Este análisis proporciona una base sólida para tomar decisiones informadas en el desarrollo del modelo.

Por ejemplo la siguiente grafica muestra el top 10 de desarolladores con el juego mas caro
![download](https://github.com/user-attachments/assets/30c343b7-415a-4d91-8d8f-cd5e36859a0a)

## Analisis de Sentimiento

Se realizó un [**análisis de sentimiento**](https://github.com/Santino-Rocchietti/P1-Steam/blob/main/sentiment_analysis.ipynb) de la columna `reviews` del archivo **users_reviews**. A través de este análisis, los comentarios fueron clasificados en tres categorías utilizando valores numéricos:

- **Comentarios positivos**: 2
- **Comentarios neutrales**: 1
- **Comentarios negativos**: 0

De esta manera, cada comentario quedó asignado a una de estas categorías. A su vez, cada juego tiene normalmente más de un comentario, que puede tomar cualquiera de los tres valores mencionados.
La siguiente nube de palabras corresponde a las palabras (lematizadas) más frecuentes en los comentarios positivos.
![download](https://github.com/user-attachments/assets/0d08f578-c34c-4a24-8cd4-4e4946096202)


## Sistema de Recomendacion

Se optó por desarrollar el **sistema de recomendación ítem-ítem**, basado en la **distancia de coseno**. A través de técnicas de **feature engineering**, cada ítem fue representado como un vector cuyas componentes corresponden a las siguientes características:

- **precio**: precio en dólares del videojuego (`float`)
- **tag_x**: serie de columnas dummie que corresponden a los tags (`binario`)
- **genre_x**: serie de columnas dummie que corresponden a los géneros (`binario`)
- **spec_x**: serie de columnas dummie que corresponden a las especificaciones (`binario`)
- **año**: año de publicación (`int`)
- **playtime_forever**: tiempo de juego histórico del ítem, escalado mediante z-score (`float`)
- **playtime_2weeks**: tiempo de juego de las últimas 2 semanas del ítem, escalado mediante z-score (`float`)
- **rating**: suma de las calificaciones (0, 1, 2) de cada ítem (`int`)
- **recommend**: suma de las recomendaciones de cada ítem (`int`)

En el siguiente [jupyter notebook](https://github.com/Santino-Rocchietti/P1-Steam/blob/main/Sistema%20de%20Recomendacion/item_item_recom.ipynb) podras encontrarlo detalladamente


## Despliegue de la API


La API se desarrolló utilizando el framework **FastAPI**, lo que permitió probar los endpoints de manera local. Posteriormente, se optó por el despliegue en **Render** para permitir el acceso desde la Web.
Puedes entrar a la API con el siguiente [link](https://p1-steam-2.onrender.com/)

Los endpoints de la API son los siguientes:

1. **Endpoint 1**: `/developer/{desarrollador}`  
   Retorna la cantidad de ítems y el porcentaje de contenido gratuito para cada año del desarrollador ingresado.

2. **Endpoint 2**: `/userdata/{user_id}`  
   Para el usuario ingresado, retorna el dinero gastado, el porcentaje de recomendación y la cantidad de ítems comprados.

3. **Endpoint 3**: `/UserForGenre/{genero}`  
   Para el género ingresado, retorna el usuario con más horas jugadas y el detalle de cuántas horas por año.

4. **Endpoint 4**: `/best_developer_year/{anio}`  
   Para el año ingresado, retorna los 3 desarrolladores con más comentarios positivos.

5. **Endpoint 5**: `/developer_reviews_analysis/{desarrolladora}`  
   Para el desarrollador ingresado, retorna la cantidad de comentarios positivos y negativos totales.

6. **Endpoint 6**: `/recomendacion_juego/{id_producto}`  
   Para el ID de producto ingresado, recomienda 5 juegos relacionados.

Recuerda que puedes consultar la documentación de la API agregando `/docs`. O ingresando [aqui](https://p1-steam-2.onrender.com/docs)

En el siguiente [video](https://youtu.be/1PR_IbBr3WA) puede verse el funcionamiento de esta API





Autor: Santino Rocchietti FT25
