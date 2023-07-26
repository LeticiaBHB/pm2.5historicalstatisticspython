import os
import pandas as pd
from tkinter import messagebox

############# comeco do programa #################

# Obtém o diretório atual
current_dir = os.getcwd()

# Lendo o arquivo csv com ponto e vírgula como delimitador
try:
    df = pd.read_csv('dadospm25.csv', sep=';', encoding='latin-1')
    messagebox.showinfo(title='Arquivo carregado', message='O arquivo foi carregado com sucesso!')
except FileNotFoundError:
    messagebox.showerror(title='Importacao CSV', message='O arquivo nao foi encontrado na pasta do executável')
    exit()  # Sai do programa caso o arquivo não seja encontrado
except Exception as e:
    messagebox.showerror(title='Importacao CSV', message=f'Ocorreu um erro ao ler o arquivo CSV: {str(e)}')
    exit()  # Sai do programa caso ocorra um erro na leitura do arquivo

# Fazendo uma cópia do DataFrame df
df_copy = df.copy()

# Substituir valores ausentes (NaN) por '-'
df_copy = df_copy.fillna('-')

# Extrair as colunas de ano da string combinada e armazená-las em colunas_existentes
colunas_anos = [str(ano) for ano in range(1990, 2020)]
colunas_existentes = [col for col in df_copy.columns if col in colunas_anos]

# Limpar e converter os valores nas colunas de ano para formato numérico
for col in colunas_existentes:
    df_copy[col] = df_copy[col].str.replace('.', '').str.replace(',', '')
    df_copy[col] = pd.to_numeric(df_copy[col], errors='coerce')  # Forçar conversão inválida para NaN

# Substituir valores NaN (causados pelos traços) por 0 para calcular a média
df_copy = df_copy.fillna(0)

# Calcular a média para cada coluna de ano (de 1990 a 2019) e armazenar em media_por_ano
media_por_ano = df_copy[colunas_existentes].mean()

# Calcular a média apenas para as colunas numéricas
df_copy['Média'] = df_copy[colunas_existentes].mean(axis=1)

# Calcular a soma total de cada linha (para as colunas de 1990 a 2020)
df_copy['Soma_Total'] = df_copy[colunas_existentes].sum(axis=1)


# Remover o caractere '-' das colunas 'Soma_Total' e 'Média'
df_copy['Soma_Total'] = df_copy['Soma_Total'].astype(str).str.replace('-', '')
df_copy['Média'] = df_copy['Média'].astype(str).str.replace('-', '')

# Criar colunas extras com os valores inteiros das somas e médias, removendo o '.' dos valores float antes de converter para int
df_copy['ValorRealSomaTotal'] = df_copy['Soma_Total'].astype(float).astype(int)
df_copy['ValorRealMedia'] = df_copy['Média'].astype(float).abs().astype(int)

# Exibir todos os nomes da tabela Country junto com as somas e médias calculadas para cada linha
result = df_copy[['Country', 'Soma_Total', 'ValorRealSomaTotal', 'Média', 'ValorRealMedia']]

# Configurar a exibição dos valores float formatados com todas as casas decimais
pd.options.display.float_format = '{:,.15f}'.format

print(result)

# Salvar o dataframe result em um arquivo CSV
result.to_csv('resultado.csv', index=False)

# Calcular a soma completa dos valores da tabela CSV de 1990 até 2020
soma_completa = df_copy[colunas_existentes].sum().sum()

# Criar um dataframe com a soma completa e a média por ano e salvar em um arquivo CSV
soma_df = pd.DataFrame({'Soma_Completa': [soma_completa]})
soma_df = soma_df.assign(**media_por_ano)

# Configurar a exibição dos valores float formatados com todas as casas decimais para a soma completa
pd.options.display.float_format = '{:,.15f}'.format

print(soma_df)

# Salvar o dataframe soma_df em um arquivo CSV
soma_df.to_csv('soma_completa.csv', index=False)

########################################################################################################
##POR CONTINENTES:

###AMÉRICA
# Filtrando as linhas que contêm "américa" na coluna "B"
filtro = df_copy['Continent'].str.contains('américa', case=False)
linhas_america = df_copy[filtro]

# Salvando as linhas relacionadas em uma nova planilha
nome_nova_planilha = 'america_dadospm25.csv'
linhas_america.to_csv(nome_nova_planilha, index=False)

print(f'Linhas relacionadas à América foram salvas em {nome_nova_planilha}.')

# Ler a nova planilha com os dados relacionados à América
nome_nova_planilha = 'america_dadospm25.csv'
df_nova_planilha = pd.read_csv(nome_nova_planilha)

# Calcular a soma dos valores da coluna 'Soma_Total'
soma_total = df_nova_planilha['Soma_Total'].sum()

# Adicionar a soma no final da planilha
nova_linha = {'Country': 'Total América', 'Soma_Total': soma_total}
df_nova_linha = pd.DataFrame([nova_linha])  # Criar um novo DataFrame com a nova linha
df_nova_planilha = pd.concat([df_nova_planilha, df_nova_linha], ignore_index=True)

# Salvar a planilha atualizada com a soma
df_nova_planilha.to_csv(nome_nova_planilha, index=False)

print(f'A soma total foi adicionada à planilha {nome_nova_planilha}.')




###ÁFRICA
# Filtrando as linhas que contêm "américa" na coluna "B"
filtro = df_copy['Continent'].str.contains('África', case=False)
linhas_africa = df_copy[filtro]

# Salvando as linhas relacionadas em uma nova planilha
nome_nova_planilha = 'africa_dadospm25.csv'
linhas_africa.to_csv(nome_nova_planilha, index=False)

print(f'Linhas relacionadas à África foram salvas em {nome_nova_planilha}.')

# Ler a nova planilha com os dados relacionados à África
nome_nova_planilha = 'africa_dadospm25.csv'
df_nova_planilha = pd.read_csv(nome_nova_planilha)

# Calcular a soma dos valores da coluna 'Soma_Total'
soma_total = df_nova_planilha['Soma_Total'].sum()

# Adicionar a soma no final da planilha
nova_linha = {'Country': 'Total África', 'Soma_Total': soma_total}
df_nova_linha = pd.DataFrame([nova_linha])  # Criar um novo DataFrame com a nova linha
df_nova_planilha = pd.concat([df_nova_planilha, df_nova_linha], ignore_index=True)

# Salvar a planilha atualizada com a soma
df_nova_planilha.to_csv(nome_nova_planilha, index=False)

print(f'A soma total foi adicionada à planilha {nome_nova_planilha}.')




###EUROPA
# Filtrando as linhas que contêm "américa" na coluna "B"
filtro = df_copy['Continent'].str.contains('europa', case=False)
linhas_europa = df_copy[filtro]

# Salvando as linhas relacionadas em uma nova planilha
nome_nova_planilha = 'europa_dadospm25.csv'
linhas_europa.to_csv(nome_nova_planilha, index=False)

print(f'Linhas relacionadas à Europa foram salvas em {nome_nova_planilha}.')

# Ler a nova planilha com os dados relacionados à Europa
nome_nova_planilha = 'europa_dadospm25.csv'
df_nova_planilha = pd.read_csv(nome_nova_planilha)

# Calcular a soma dos valores da coluna 'Soma_Total'
soma_total = df_nova_planilha['Soma_Total'].sum()

# Adicionar a soma no final da planilha
nova_linha = {'Country': 'Total Europa', 'Soma_Total': soma_total}
df_nova_linha = pd.DataFrame([nova_linha])  # Criar um novo DataFrame com a nova linha
df_nova_planilha = pd.concat([df_nova_planilha, df_nova_linha], ignore_index=True)

# Salvar a planilha atualizada com a soma
df_nova_planilha.to_csv(nome_nova_planilha, index=False)

print(f'A soma total foi adicionada à planilha {nome_nova_planilha}.')




###ÁSIA
# Filtrando as linhas que contêm "américa" na coluna "B"
filtro = df_copy['Continent'].str.contains('ásia', case=False)
linhas_asia = df_copy[filtro]

# Salvando as linhas relacionadas em uma nova planilha
nome_nova_planilha = 'asia_dadospm25.csv'
linhas_asia.to_csv(nome_nova_planilha, index=False)

print(f'Linhas relacionadas à Ásia foram salvas em {nome_nova_planilha}.')

# Ler a nova planilha com os dados relacionados à Ásia
nome_nova_planilha = 'asia_dadospm25.csv'
df_nova_planilha = pd.read_csv(nome_nova_planilha)

# Calcular a soma dos valores da coluna 'Soma_Total'
soma_total = df_nova_planilha['Soma_Total'].sum()

# Adicionar a soma no final da planilha
nova_linha = {'Country': 'Total América', 'Soma_Total': soma_total}
df_nova_linha = pd.DataFrame([nova_linha])  # Criar um novo DataFrame com a nova linha
df_nova_planilha = pd.concat([df_nova_planilha, df_nova_linha], ignore_index=True)

# Salvar a planilha atualizada com a soma
df_nova_planilha.to_csv(nome_nova_planilha, index=False)

print(f'A soma total foi adicionada à planilha {nome_nova_planilha}.')




###OCEANIA
# Filtrando as linhas que contêm "américa" na coluna "B"
filtro = df_copy['Continent'].str.contains('oceania', case=False)
linhas_oceania = df_copy[filtro]

# Salvando as linhas relacionadas em uma nova planilha
nome_nova_planilha = 'oceania_dadospm25.csv'
linhas_oceania.to_csv(nome_nova_planilha, index=False)

print(f'Linhas relacionadas à Oceania foram salvas em {nome_nova_planilha}.')

# Ler a nova planilha com os dados relacionados à América
nome_nova_planilha = 'oceania_dadospm25.csv'
df_nova_planilha = pd.read_csv(nome_nova_planilha)

# Calcular a soma dos valores da coluna 'Soma_Total'
soma_total = df_nova_planilha['Soma_Total'].sum()

# Adicionar a soma no final da planilha
nova_linha = {'Country': 'Total Oceania', 'Soma_Total': soma_total}
df_nova_linha = pd.DataFrame([nova_linha])  # Criar um novo DataFrame com a nova linha
df_nova_planilha = pd.concat([df_nova_planilha, df_nova_linha], ignore_index=True)

# Salvar a planilha atualizada com a soma
df_nova_planilha.to_csv(nome_nova_planilha, index=False)

print(f'A soma total foi adicionada à planilha {nome_nova_planilha}.')


#SOMAS TOTAIS AGRUPADAS:

# Filtrar as linhas para cada continente e calcular as somas totais
continentes = ['américa', 'África', 'europa', 'ásia', 'oceania']
somas_totais = []

for continente in continentes:
    filtro = df_copy['Continent'].str.contains(continente, case=False)
    linhas_continente = df_copy[filtro]
    soma_total = linhas_continente['Soma_Total'].sum()
    somas_totais.append({'Continente': continente, 'Soma_Total': soma_total})

# Criar um DataFrame com as somas totais
df_somas_totais = pd.DataFrame(somas_totais)

# Salvar as somas totais em uma nova planilha
nome_nova_planilha_total = 'somas_totais_dadospm25.csv'
df_somas_totais.to_csv(nome_nova_planilha_total, index=False)

print(f'Somas totais foram salvas na planilha {nome_nova_planilha_total}.')

