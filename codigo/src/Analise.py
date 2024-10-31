import pandas as pd

# Carregar os dados do CSV
df_commits = pd.read_csv('./codigo/dados/hexo-DADOS.csv')

# Visualizar os dados
print(df_commits.head())

# Adicionar uma coluna fictícia para Code Coverage
df_commits['code_coverage'] = 0.85  # Exemplo: 85% de cobertura

# Simulação de dados de tempo para detecção (dias)
# Você precisará ajustar isso com base em dados reais
df_commits['defect_detection_time'] = (pd.to_datetime(df_commits['date']) - pd.to_datetime('2024-01-01')).dt.days

# Calcular a média do tempo de detecção
mean_detection_time = df_commits['defect_detection_time'].mean()
print(f'Tempo médio para detecção de defeitos: {mean_detection_time} dias')

# Agrupando por autor e calculando a média das métricas
grouped_df = df_commits.groupby('author').agg({
    'code_coverage': 'mean',
    'defect_detection_time': 'mean'
}).reset_index()

print(grouped_df)

from scipy.stats import spearmanr

# Supondo que você tenha outra métrica para comparar (popularidade, complexidade, etc.)
# Adicione uma coluna fictícia para popularidade
df_commits['popularity'] = df_commits.index % 100  # Exemplo: valores aleatórios

# Calcular a correlação de Spearman
correlation, p_value = spearmanr(df_commits['code_coverage'], df_commits['popularity'])
print(f'Correlação de Spearman: {correlation}, P-Value: {p_value}')
