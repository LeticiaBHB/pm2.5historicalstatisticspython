import os
import pandas as pd
from tkinter import messagebox

############# comeco do programa #################

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

# Substituir valores NaN (causados pelos traços) por 0 para calcular a média
df = df.fillna(0)

# Configurar a exibição dos valores float formatados
pd.set_option('display.float_format', '{:.15g}'.format)

# Calcular a média para cada coluna de ano (de 1990 a 2019) e armazenar em media_por_ano
media_por_ano = df[colunas_existentes].mean()
print(media_por_ano)

# Calcular a média apenas para as colunas numéricas
df['Média'] = df[colunas_existentes].mean(axis=1)

# Configurar a exibição dos valores float formatados
pd.set_option('display.float_format', '{:.15f}'.format)

# Calcular a soma total de cada linha (para as colunas de 1990 a 2020)
df['Soma_Total'] = df[colunas_existentes].sum(axis=1)

# Exibir todos os nomes da tabela Country junto com a média calculada para cada linha
result = df[['Country', 'Soma_Total', 'Média']]

print(result)

# Calcular a soma completa dos valores da tabela CSV de 1990 até 2020
soma_completa = df[colunas_existentes].sum().sum()

# Salvar o dataframe result em um arquivo CSV
result.to_csv('resultado.csv', index=False)

# Criar um dataframe com a soma completa e salvar em um arquivo CSV
soma_df = pd.DataFrame({'Soma_Completa': [soma_completa]})
soma_df.to_csv('soma_completa.csv', index=False, float_format='%.15f')
