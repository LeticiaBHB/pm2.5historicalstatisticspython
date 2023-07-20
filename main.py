import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox

############# Início do programa #################

# Obtém o diretório atual
current_dir = os.getcwd()

# Lendo o arquivo csv com ponto e vírgula como delimitador
try:
    df = pd.read_csv('dadospm25.csv', sep=';')
    messagebox.showinfo(title='Arquivo carregado', message='O arquivo foi carregado com sucesso!')
except:
    messagebox.showerror(title='Importacao CSV', message='O arquivo nao esta na pasta do executável')

# Substituir valores ausentes (NaN) por '-'
df = df.fillna('-')

# Extrair as colunas de ano da string combinada e armazená-las em colunas_existentes
colunas_anos = [str(ano) for ano in range(1990, 2020)]
colunas_existentes = [col for col in df.columns if col in colunas_anos]

# Limpar e converter os valores nas colunas de ano para formato numérico
for col in colunas_existentes:
    df[col] = df[col].str.replace('.', '').str.replace(',', '')
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Forçar conversão inválida para NaN

# Configurar a exibição dos valores float formatados
pd.set_option('display.float_format', '{:.15g}'.format)

# Calcular a média para cada coluna de ano (de 1990 a 2019) e armazenar em media_por_ano
media_por_ano = df[colunas_existentes].mean()
print(media_por_ano)

# Calcular a média apenas para as colunas numéricas
df['Média'] = df[colunas_existentes].mean(axis=1)

# Configurar a exibição dos valores float formatados

# Exibir todos os nomes da tabela Country junto com a média calculada para cada linha
result = df[['Country', 'Média']]
print(result)

# Salvar o dataframe media_por_ano em um arquivo CSV
media_por_ano.to_csv('media_por_ano.csv', index=False)

# Salvar o dataframe result em um arquivo CSV
result.to_csv('resultado.csv', index=False)
