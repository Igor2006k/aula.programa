import sqlite3
conn = sqlite3.connect('sala.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS produto (idproduto integer primary key AUTOINCREMENT,nome TEXT,category TEXT,valor NUMERIC)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas (idpessoas integer primary key AUTOINCREMENT,nome TEXT,email TEXT,cidade TEXT,idade TEXT)''')
def gravar_produto(nome, category, valor):
    cursor.execute('''
        INSERT INTO produto (nome, category, valor) VALUES (?, ?, ?)''', (nome, category, valor))
    conn.commit()
gravar_produto('yogurte', 'comida', 5.2)
gravar_produto('Sabão', 'limpeza', 2.90)
gravar_produto('escova', 'limpeza', 3.15)
gravar_produto('mamão', 'comida', 4.90)

def gravar_pessoas(nome, email, cidade, idade):
    cursor.execute('''
        INSERT INTO pessoas (nome, email, cidade, idade) VALUES (?, ?, ?, ?)''', (nome, email, cidade, idade))
    conn.commit()
gravar_pessoas('igor', 'igor@gmail.com', 'pedro ii', 17)
gravar_pessoas('daniel', 'daniel@gmamil.com', 'pedro ii', 16)
gravar_pessoas('matheus', 'matheus@gmail.com', 'pedro ii', 17)
gravar_pessoas('bruno', 'bruno@gmail.com', 'pedro ii', 11)