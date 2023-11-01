from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
def conexao():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn
#route --rota que desejo usar
@app.route('/')
def ola_mundo():
	return "Ola mundo"

@app.route('/home')
def home():
    conn = conexao()
	dados = conn.execute('SELECT * FROM dados').fetchall()
	return render_template('index.html', dados=dados)
if __name__ == "__main__":
	app.run(debug=True)