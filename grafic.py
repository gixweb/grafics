import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('StressLevelDataset.csv')

#Só pra ver as métricas do dataset
print("Primeiras 5 linhas do DataFrame:")
print(df.head())

print("\nEstatísticas descritivas da coluna 'stress_level':")
print(df['stress_level'].describe())

print("\nValores únicos na coluna 'stress_level':")
print(df['stress_level'].unique())

print("\nContagem de valores na coluna 'stress_level':")
print(df['stress_level'].value_counts())

# Criar o histograma de barras
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='stress_level', bins=10, kde=False)
plt.title('Histograma da Distribuição do Nível de Estresse')
plt.xlabel('Nível de Estresse')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Criar a curva de densidade de dados
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='stress_level', fill=True, color='purple')
plt.title('Curva de Densidade do Nível de Estresse')
plt.xlabel('Nível de Estresse')
plt.ylabel('Densidade')
plt.show()

# Criar o boxplot com outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='stress_level')
plt.title('Boxplot do Nível de Estresse (com Outliers)')
plt.ylabel('Nível de Estresse')
plt.show()

# Calcular o IQR e os limites dos outliers
Q1 = df['stress_level'].quantile(0.25)
Q3 = df['stress_level'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Criar um novo DataFrame sem os outliers
df_no_outliers = df[(df['stress_level'] >= lower_bound) & (df['stress_level'] <= upper_bound)]

# Criar o boxplot sem outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_no_outliers, y='stress_level')
plt.title('Boxplot do Nível de Estresse (sem Outliers)')
plt.ylabel('Nível de Estresse')
plt.show()
