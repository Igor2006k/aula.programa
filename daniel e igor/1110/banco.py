import sqlite3
conn = sqlite3.connect('sala.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS dados (nome TEXT,veiculo INTEGER,id INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS dados (nome TEXT,veiculo INTEGER,id INTEGER)''')
def gravar_dado(nome, idade, id):
    cursor.execute('''
        INSERT INTO dados (marca, veiculo, nome)
        VALUES (?, ?, ?
        )
    ''', (nome, idade, id))
    conn.commit()
def obter_dados():
    cursor.execute('''
        SELECT * FROM dados
    ''')
    return cursor.fetchall()
gravar_dado('veiculo', 13, 1)
gravar_dado('nome', 11, 2)
gravar_dado('marca', 12, 3)
gravar_dado('estado', 9, 4)