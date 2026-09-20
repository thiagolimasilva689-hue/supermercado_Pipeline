import pandas as pd
df = pd.read_csv(r'C:\Users\Thiago\OneDrive\Desktop\teiu\primeira_pipeline\vendas_supermercado.csv')
#VENDO QUANTOS VALORES NULOS EM CADA COLUNA
#print(df.isna().sum())

# CRIAR CÓPIA
df_Preenchido = df.copy()

# TRATAR PRODUTO VAZIO (remover)
df_Preenchido = df_Preenchido.dropna(subset=['produto'])

#PREENCHENDO OS VALORES
df_Preenchido['produto'] = df_Preenchido['produto'].fillna("não informado")
df_Preenchido['categoria'] = df_Preenchido['categoria'].fillna("não informado")
df_Preenchido['preco'] = df_Preenchido['preco'].fillna(df_Preenchido['preco'].median())
#ELIMINADO DUPLICADAS
df_Preenchido = df_Preenchido.drop_duplicates()
#CONVERTO PARA TIPO DATATIME
df_Preenchido['data'] = pd.to_datetime(df_Preenchido['data'])

#Criando uma nova coluna
df_Preenchido['valor_total'] = df_Preenchido['preco'] * df_Preenchido['quantidade']

#vendo o resultado
print("\nDataFrame limpo:")
print(df_Preenchido)

#Criando arquivo limpo
df_Preenchido.to_csv(r'C:\Users\Thiago\OneDrive\Desktop\teiu\primeira_pipeline\vendas_limpo.csv', index=False)
