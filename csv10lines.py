import pandas as pd

# Nome do arquivo CSV de entrada
input_csv = 'deepmind_code_contests.csv'

# Nome do arquivo CSV de saída
output_csv = 'deepmind_code_contests_10lines.csv'
# Define o tamanho do chunk para carregar os dados em partes
chunksize = 1000

# Lista para armazenar as primeiras 10 linhas
first_10_lines = []

# Leitura incremental do arquivo CSV
for chunk in pd.read_csv(input_csv, chunksize=chunksize):
    # Adiciona as linhas do chunk à lista, até que tenhamos 10 linhas
    for index, row in chunk.iterrows():
        if len(first_10_lines) < 10:
            first_10_lines.append(row)
        else:
            break
    if len(first_10_lines) >= 10:
        break

# Converte a lista de linhas em um DataFrame
df_first_10 = pd.DataFrame(first_10_lines)

# Escreve o DataFrame em um novo arquivo CSV
df_first_10.to_csv(output_csv, index=False)

print("Novo arquivo CSV com 10 linhas criado com sucesso.")