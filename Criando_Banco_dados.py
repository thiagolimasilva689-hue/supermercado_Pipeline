import sqlite3
import pandas as pd
# Conectar ao banco
conexao = sqlite3.connect('supermercado')
cursor = conexao.cursor()

#criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
               data TEXT,
               produto TEXT,
               categoria TEXT,
               preco REAL,
               quantidade INT,
               vendedor TEXT,
               regiao TEXT,
               valor_total REAL)
''')
# LER CSV LIMPO
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\primeira_pipeline\vendas_limpo.csv'
df = pd.read_csv(caminho)

# CONECTAR
conexao = sqlite3.connect('supermercado.db')

# INSERIR DIRETO (Pandas faz tudo)
df.to_sql('produtos', conexao, if_exists='replace', index=False)

# VERIFICAR
cursor = conexao.cursor()
cursor.execute("SELECT * FROM produtos LIMIT 5")
for produto in cursor.fetchall():
    print(produto)

# FECHAR
conexao.close()
print("\nDados inseridos com sucesso!")

