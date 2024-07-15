from datasets import load_dataset
import pandas as pd

# Carregar o dataset DeepMind Code Contests do Hugging Face
dataset = load_dataset('deepmind/code_contests')

# Nome do arquivo CSV de saída
output_csv = 'deepmind_code_contests.csv'

# Inicializa o arquivo CSV com o cabeçalho dos dados
pd.DataFrame(dataset['train'][0:0]).to_csv(output_csv, index=False)

# Define o tamanho do lote para carregar e salvar os dados em partes
batch_size = 1000

# Itera sobre o dataset em lotes
for i in range(0, len(dataset['train']), batch_size):
    # Carrega uma parte do dataset
    batch = dataset['train'][i:i + batch_size]
    
    # Converte a parte do dataset em um DataFrame do pandas
    df_batch = pd.DataFrame(batch)
    
    # Salva a parte do DataFrame no arquivo CSV, adicionando ao final do arquivo
    df_batch.to_csv(output_csv, mode='a', header=False, index=False)

print("Dataset exportado incrementalmente com sucesso para 'deepmind_code_contests.csv'")