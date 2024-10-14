
![images](https://github.com/user-attachments/assets/2c559b96-5d09-48dd-b395-111783fee614)


# Proyecto integrador 1 Steam:

### En este repositorio se podra visualizar el primer proyecto integrador del Bootcamp Henry para Data Science.



## Objetivo


### Situándonos en el rol de Data Scientist, desarrollaremos un Sistema de Recomendación para la plataforma de videojuegos online Steam Games. 

### El MVP debe desplegarse como una API que pueda ser consumida desde la Web.



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




Luego de realizada la **limpieza de los datos**, se llevó a cabo un [**Análisis Exploratorio de Datos (EDA)**](https://github.com/Santino-Rocchietti/P1-Steam/blob/main/EDA_steam.ipynb). El objetivo del análisis es entender las relaciones entre los diferentes datos, encontrar insights que permitan mejorar la interpretación de los mismos y retroalimentar el desarrollo del modelo con nuevas perspectivas.

En el notebook encontrarás visualizaciones que muestran información interesante, como:

- Qué géneros de juegos son los más consumidos
- Cuáles son los juegos más caros
- Qué palabras son las más frecuentes en los títulos

Este análisis proporciona una base sólida para tomar decisiones informadas en el desarrollo del modelo.

Por ejemplo la siguiente grafica muestra el top 10 de desarolladores con el juego mas caro
![download](https://github.com/user-attachments/assets/30c343b7-415a-4d91-8d8f-cd5e36859a0a)

