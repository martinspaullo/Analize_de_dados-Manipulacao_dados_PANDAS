import pandas as pd
import matplotlib.pyplot as plt

#1-Criando Dataframe de Exemplo
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Idade':[25, 30, 35, 40, 27],
    'Cargo':['Analista', 'Gerente', 'CEO', 'Analista', 'Coordenador'],
    'Salario':[5000, 8000, 15000, 4800, 6000]
}

df = pd.DataFrame(data)

print(df)

#2-Visualizando primeiras linhas do DataFrame
print(df.head(2))

#3-Informações sobre o DataFrame
print(df.info())

#4-Estastística Descritiva
print(df.describe())

#5-Condição em Dataframe (salário > 5000)
print(df[df['Salario'] > 5000])

#6-Ordenação (pela Idade)
print(df.sort_values(by='Idade', ascending=False))

#7-Adicionando coluna calculada
df['Bonus'] = df['Salario'] * 0.1
print(df)

#7.1 - Valor total geral sem bonus
print(f"Valor total sem bonus: {df['Salario'].sum()}")

# 7.2 - Valor total de bônus
valor_total_bonus = df['Bonus'].sum()
print(f"Valor total bonus: {valor_total_bonus}")

# 7.3 - Valor total de salários + bônus
valor_total_geral = df['Salario'].sum() + valor_total_bonus
print(f"Valor total geral com bonus: {valor_total_geral}")

#8-Agrupamento e agregação
print(df.groupby('Cargo')['Salario'].mean())

#9-Visualização básica
df.plot(
    kind='bar',
    x='Nome',
    y='Salario',
    title='Salário dos Funcionários',
    rot=45
)

plt.show()
