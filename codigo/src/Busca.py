import requests
import pandas as pd
import os

# Substitua com o seu token pessoal
TOKEN = ''

# Defina os repositórios e seus respectivos proprietários
repos = [
    {'owner': 'hexojs', 'name': 'hexo'},
    {'owner': 'mmistakes', 'name': 'minimal-mistakes'},
    {'owner': 'tac0x2a', 'name': 'simple-blockchain'},
    {'owner': 'freeCodeCamp', 'name': 'curriculum'},
    {'owner': 'Kong', 'name': 'insomnia'},
    {'owner': 'HospitalRun', 'name': 'hospitalrun-frontend'},
    {'owner': 'jitsi', 'name': 'jitsi-meet'},
    {'owner': 'electron', 'name': 'electron'},
    {'owner': 'microsoft', 'name': 'vscode'}
]

# Cabeçalhos para a requisição, incluindo o token de autenticação
headers = {
    'Authorization': f'Token {TOKEN}'
}

# Função para buscar commits de um repositório
def fetch_commits(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        commits_data = response.json()
        commits_list = []
        
        for commit in commits_data:
            commit_info = {
                'sha': commit['sha'],
                'author': commit['commit']['author']['name'],
                'date': commit['commit']['author']['date'],
                'message': commit['commit']['message']
            }
            commits_list.append(commit_info)
        
        # Retornar DataFrame com os commits
        return pd.DataFrame(commits_list)
    else:
        print(f'Erro: {response.status_code} ao acessar {owner}/{repo}')
        return pd.DataFrame()

# Criar o diretório 'dados' caso não exista
os.makedirs('./codigo/dados', exist_ok=True)

# Iterar pelos repositórios e salvar os commits de cada um
for repo in repos:
    owner = repo['owner']
    name = repo['name']
    
    print(f'Buscando commits para {owner}/{name}...')
    df_commits = fetch_commits(owner, name)
    
    if not df_commits.empty:
        csv_file_name = f'./codigo/dados/{name}-DADOS.csv'
        df_commits.to_csv(csv_file_name, index=False)
        print(f'Dados de {name} salvos em {csv_file_name}')
    else:
        print(f'Sem dados para {name}')
