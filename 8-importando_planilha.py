import pandas as pd

#Caminho para o arquivo Excel
caminho_arquivo = "data/livros.xlsx"
df = pd.read_excel(caminho_arquivo)

print(df)

#1-Visão geral dos dados
print(df.head())  # first record
print(df.tail())  # last record

#2-Verificando tipos de dados
print(df.dtypes)

#3-Estatísticas Descritivas
print(df.describe())
print(df[['Preço (R$)', 'Quantidade']].describe())
