from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

DATABASE = 'banco.db'

def conectar_bd():
	return sqlite3.connect(DATABASE)

with conectar_bd() as con:
	con.execute('''CREATE TABLE IF NOT EXISTS pessoa (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT)''')
@app.route('/')
def listar():
	with conectar_bd() as con:
		registros = con.execute('Select * From pessoa').fetchall()
	return render_template('index.html', registros=registros)
if __name__== '__main__':
	app.run(debug=True)