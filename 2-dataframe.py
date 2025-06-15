import pandas as pd

#1-Dados ds times e suas quantidades de títulos
dados_titulos = {
    'Real Madrid': 34,
    'Barcelona':26,
    'Liverpool':19,
    'Juventus':36,
    'Bayern Munich':30
}

#2-Ano do título
dados_anos = {
    'Real Madrid': [1956, 1957, 1958, 1959, 1960],
    'Barcelona':[1992, 2006, 2009, 2011, 2015],
    'Liverpool':[1977, 1978, 1981, 1984, 2005],
    'Juventus':[1958, 1985, 1996, 2011, 2015],
    'Bayern Munich':[1974, 1975, 1976, 2001, 2013]
}

#3-Criando a Series
series_titulos = pd.Series(dados_titulos)
series_anos = pd.Series(dados_anos)

print(series_titulos)
print(series_anos)

#4-Criando Dataframe combinando as Series
data = {'Títulos': series_titulos, 'Anos':series_anos}
dataframe_times = pd.DataFrame(data)

#5-Exibindo o DataFrame
print(dataframe_times)
