import sqlite3
conn = sqlite3.connect('mateit.db')
cursor = conn.cursor()
#cursor.execute('''create table pessoa(nome TEXT,idade INTEGER)''')
def gravar (nome,idade):
    cursor.execute ('''INSERT INTO pessoa (nome,idade)VALUES(?,?)''',(nome,idade))
    conn.commit()
    
gravar("Bia",18)