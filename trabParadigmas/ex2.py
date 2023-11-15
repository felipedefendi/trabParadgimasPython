import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'games.csv'
df = pd.read_csv(file_path)

df.head()

df_filter = df[df['Year'] > 2000]

df_filter2 = df[df['Genre'] == 'Action']

# Geração de gráficos

# Gráfico 1: Contagem de jogos por plataforma
plt.figure(figsize=(12, 6))
sns.countplot(x='Platform', data=df_filter)
plt.title('Contagem de Jogos por Plataforma (pós-2000)')
plt.xlabel('Plataforma')
plt.ylabel('Contagem')
plt.show()

# Gráfico 2: Vendas globais por ano
plt.figure(figsize=(12, 6))
df_grouped_by_year = df.groupby('Year')['Global_Sales'].sum().reset_index()
sns.lineplot(x='Year', y='Global_Sales', data=df_grouped_by_year)
plt.title('Vendas Globais ao longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Vendas Globais (em milhões)')
plt.show()

# Gráfico 3: Vendas globais médias por gênero
plt.figure(figsize=(12, 6))
df_grouped_by_genre = df.groupby('Genre')['Global_Sales'].mean().reset_index()
sns.barplot(x='Genre', y='Global_Sales', data=df_grouped_by_genre)
plt.title('Vendas Globais Médias por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Vendas Globais Médias (em milhões)')
plt.show()