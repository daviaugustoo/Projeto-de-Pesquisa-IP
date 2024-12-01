import os
import pandas as pd
import re

def calcular_metricas_por_arquivo():
    """
    Calcula as métricas de qualidade de software separadamente para cada arquivo CSV na pasta 'dados'
    e gera uma tabela consolidada com os resultados.
    """

    diretorio = './codigo/dados'

    # Verifica se o diretório existe
    if not os.path.isdir(diretorio):
        print(f"Erro: O diretório '{diretorio}' não existe.")
        return

    # Lista para armazenar os resultados por arquivo
    resultados_por_arquivo = []

    def calculate_defect_post_production_rate(file_path):
        data = pd.read_csv(file_path)
        total_commits = len(data)
        data['message'] = data['message'].fillna('')  # Preenche valores nulos com string vazia
        refactor_count = data['message'].str.count('refactor', flags=re.IGNORECASE).sum()
        chore_count = data['message'].str.count('chore', flags=re.IGNORECASE).sum()
        total_defects = refactor_count + chore_count
        return total_defects / total_commits if total_commits > 0 else 0

    # Percorre todos os arquivos CSV no diretório
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            df = pd.read_csv(caminho_arquivo)

            # Valida a presença das colunas esperadas
            colunas_esperadas = {'sha', 'author', 'date', 'message'}
            if not colunas_esperadas.issubset(df.columns):
                print(f"Arquivo {arquivo} ignorado: colunas esperadas não encontradas.")
                continue

            # Trata valores nulos
            df.fillna("", inplace=True)

            # Inicializa as métricas para este arquivo
            total_comits = len(df)
            total_desenvolvedores = df['author'].nunique()
            
            # Conversão de datas para calcular duração do projeto
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            if not df['date'].isnull().all():
                duracao_projeto = (df['date'].max() - df['date'].min()).days
            else:
                duracao_projeto = 0

            # Identifica mensagens com tags de refatoração
            total_tags_refatoracao = df[df['message'].str.contains('refactor|chore', case=False, na=False)]['message'].count()

            # Calcula as métricas para este arquivo
            comits_por_desenvolvedor = total_comits / total_desenvolvedores if total_desenvolvedores else 0
            tempo_medio_resolucao = duracao_projeto  # Cada arquivo é tratado como um projeto único
            densidade_defeitos = calculate_defect_post_production_rate(caminho_arquivo)  # Caminho do arquivo CSV
            taxa_defeitos_pos_producao = total_tags_refatoracao / total_comits if total_comits else 0

            # Adiciona os resultados à lista
            resultados_por_arquivo.append({
                'Arquivo': arquivo,
                'Comits por Desenvolvedor': comits_por_desenvolvedor,
                'Tempo Médio de Resolução (dias)': tempo_medio_resolucao,
                'Densidade dos Defeitos': densidade_defeitos,
                'Taxa de Defeitos Pós-Produção': taxa_defeitos_pos_producao
            })

    # Converte a lista de resultados em um DataFrame
    tabela_resultados = pd.DataFrame(resultados_por_arquivo)

    # Exibe a tabela no console
    print("Tabela Consolidada de Métricas:")
    print(tabela_resultados)

    # Exporta para um arquivo CSV
    caminho_saida = os.path.join(diretorio, '../metricas_consolidadas.csv')
    tabela_resultados.to_csv(caminho_saida, index=False)
    print(f"Tabela consolidada salva em: {caminho_saida}")

# Chama a função
calcular_metricas_por_arquivo()
