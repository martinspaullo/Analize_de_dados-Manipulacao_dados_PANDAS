"""
Funcionalidades de Series:
1-Armazenamento de Dados Unidimensionais
2-Utilizado em Operações Vetorizada
3-Focado em Dados Estruturados
"""
import pandas as pd

#1-Dados ds times e suas quantidades de títulos
dados = {
    'Real Madrid': 34,
    'Barcelona':26,
    'Liverpool':19,
    'Juventus':36,
    'Bayern Munich':30
}

#2-Criando a serie a partir de um dicionário
series_times = pd.Series(dados)
print(series_times)
print(type(series_times))

#3-Selecionar time por índice
print(series_times['Juventus'])
print(series_times.iloc[2])

#4-Selecionando por Fatiamento
print('\n')
print(series_times['Barcelona':'Juventus']) # inclusivo

#5-Selecionando por condição
print('\n')
print(series_times[series_times > 30])