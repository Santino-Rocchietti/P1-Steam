import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/recommend/{item_id}")
def item_item_recom(item_id: int, n_recom: int = 5, umbral: float = 0.999):
    try:
        df_names = pd.read_parquet('Sistema de Recomendacion/item_names.parquet')

        if item_id not in df_names['id'].values:
            raise HTTPException(status_code=400, detail='Ingrese un id de producto válido')

        indice = df_names[df_names['id'] == item_id].index[0]
        df_items = pd.read_parquet('Sistema de Recomendacion/item_item_features.parquet')

        # Convertir las columnas a tipo numérico
        df_items = df_items.apply(pd.to_numeric, errors='coerce')

        # Elimina filas con valores NaN o no válidos
        df_items.dropna(inplace=True)

        similaridades = {}
        contador = 0

        for i in range(len(df_items)):
            if i != indice:
                try:
                    sim = cosine_similarity(
                        df_items.iloc[indice, :].values.reshape(1, -1),
                        df_items.iloc[i, :].values.reshape(1, -1)
                    )[0][0]
                    similaridades[i] = sim
                    if sim > umbral:
                        contador += 1
                    if contador > n_recom:
                        break
                except ValueError:
                    continue

        similaridades_sorted = sorted(similaridades.items(), key=itemgetter(1), reverse=True)

        items_recomendados = []
        for i in range(min(n_recom, len(similaridades_sorted))):
            idx = similaridades_sorted[i][0]
            items_recomendados.append({
                'item_id': df_names.loc[idx, 'id'],
                'app_name': df_names.loc[idx, 'app_name']
            })

        return {"recommendations": items_recomendados}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Ocurrió un error inesperado: {str(e)}')
