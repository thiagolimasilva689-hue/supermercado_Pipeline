import sqlite3
import pandas as pd

# CONECTAR NO SQLITE
conexao = sqlite3.connect(r'C:\Users\Thiago\OneDrive\Desktop\teiu\primeira_pipeline\supermercado.db')

# LER A TABELA
df = pd.read_sql('SELECT * FROM produtos', conexao)

# SALVAR COMO CSV
df.to_csv(r'C:\Users\Thiago\OneDrive\Desktop\teiu\primeira_pipeline\vendas_powerbi.csv', index=False,decimal=',', sep=';')

# FECHAR
conexao.close()

print("CSV exportado com sucesso!")
print(df.head())
