from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

DATABASE = 'agenda.db'

def conectar_bd():
    return sqlite3.connect(DATABASE)


with conectar_bd() as con:
    con.execute('''CREATE TABLE IF NOT EXISTS pessoas
    (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT)''')
@app.route('/')
def listar():
	with conectar_bd as con:
		registros = con.execute('SELECT * FROM pessoas').fetchall()
	return render_template('listagem.html', registros=registros)
if __name__ == '__main__':
	app.run(debug=True)