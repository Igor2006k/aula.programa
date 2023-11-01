import sqlite3
conn = sqlite3.connect("product.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE dados (idp INT, nome TEXT, valor BOOL, category TEXT)''')

def gravar_dado(idp,nome,valor,category):
    cursor.execute('''
        INSERT INTO dados (idp,nome,valor,category)
        VALUES (?, ?, ?, ?)
    ''', (idp,nome,valor,category))
    conn.commit()
def obter_dados():
    cursor.execute('''
        SELECT * FROM dados
    ''')
    return cursor.fetchall()

gravar_dado( 1, 'arroz', 6.30, 'alimento')
gravar_dado( 2, 'feijao', 15.30, 'alimento')
gravar_dado( 3, 'sabao', 2.30, 'limpeza')
gravar_dado( 4, 'esponja', 0.30, 'limpeza')
gravar_dado( 5, 'biscoito', 2.30, 'alimento')
