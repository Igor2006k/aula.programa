import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS produto (idproduto integer primary key AUTOINCREMENT,nome TEXT,category TEXT,valor NUMERIC)''')
def gravar_dados(nome,category,veicolu):
    cursor.execute('''
        INSERT INTO veiculo (nome, category,veiculo )
        VALUES (?, ?, ?)
    ''', (nome,category,VEICULO))
    conn.commit()
def obter_dados():
    cursor.execute('''
        SELECT * FROM VEICULO
    ''')
    return cursor.fetchall()
gravar_dados('veiculo','',6.90)
gravar_dados('nome', 'alimento',15.0)
gravar_dados('marca', 'esportes',90.8)
gravar_dados('estado','alimento',6.50)