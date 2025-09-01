import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\gisel\OneDrive\Documentos\codesDocs\StressLevelDataset.csv')

print(df.columns)

# Criar o histograma de barras
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='stress level', bins=10, kde=False)
plt.title('Histograma da Distribuição do Nível de Estresse')
plt.xlabel('Nível de Estresse')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Criar a curva de densidade de dados
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='stress level', fill=True, color='purple')
plt.title('Curva de Densidade do Nível de Estresse')
plt.xlabel('Nível de Estresse')
plt.ylabel('Densidade')
plt.show()

# Criar o boxplot com outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='stress level')
plt.title('Boxplot do Nível de Estresse (com Outliers)')
plt.ylabel('Nível de Estresse')
plt.show()

# Calcular o IQR e os limites dos outliers
Q1 = df['stress level'].quantile(0.25)
Q3 = df['stress level'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Criar um novo DataFrame sem os outliers
df_no_outliers = df[(df['stress level'] >= lower_bound) & (df['stress level'] <= upper_bound)]

# Criar o boxplot sem outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_no_outliers, y='stress level')
plt.title('Boxplot do Nível de Estresse (sem Outliers)')
plt.ylabel('Nível de Estresse')
plt.show()