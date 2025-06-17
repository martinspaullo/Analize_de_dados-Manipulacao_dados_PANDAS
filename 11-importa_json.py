import pandas as pd

#1-Importando o arquivo Json
df = pd.read_json("data/series.json")

print(df)

#2-Utilizando o json_normalize para aplanar dados aninhados
df_series = pd.json_normalize(
    df['series'],
    'temporadas',
    ['titulo', 'genero', 'ano_lancamento']
)

print(df_series)
