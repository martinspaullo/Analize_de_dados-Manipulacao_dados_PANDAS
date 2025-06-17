import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///pedidos.db')

#1-TOtal de Vendas por Região
consulta_1 = "SELECT Regiao, SUM(Unidades) AS Total_Unidades_Vendidas FROM pedidos GROUP BY Regiao"
resultado_1 = pd.read_sql_query(consulta_1, engine)
print("Total de Vendas por região:\n")
print(resultado_1)

#2-Vendedor com o maior número de vendas
consulta_2 = "SELECT Vendedor, SUM(Unidades) AS Total_Unidades_Vendidas FROM pedidos GROUP BY Vendedor ORDER BY Total_Unidades_Vendidas DESC LIMIT 3"
resultado_2 = pd.read_sql_query(consulta_2, engine)
print("Vendedor com o maior número de vendas")
print(resultado_2)

#3-Total de Vendas por Item
consulta_3 = "SELECT Item, SUM(Unidades) AS Total_Unidades_Vendidas FROM pedidos GROUP BY Item ORDER BY Total_Unidades_Vendidas DESC" 
resultado_3 = pd.read_sql_query(consulta_3, engine)
print("Total de vendas por item:")
print(resultado_3)

#4-Média de Preço por Item
consulta_4 = "SELECT Item, AVG(PrecoUnidade) AS Media_Preco_Unidade FROM pedidos GROUP BY Item"
resultado_4 = pd.read_sql_query(consulta_4, engine)
print("media de preco por item:")
print(resultado_4)
