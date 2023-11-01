from flask import Flask, render_template

import sqlite3

app = Flask(__name__)

def conexao():
	conn = sqlite3.connect("sala.db")
	conn.row_factory = sqlite3.Row
	return conn
@app.route('/')
def home():
	conn = conexao()
	dados = conn.execute("Select * FROM dados").fetchall()
	conn.close()
	return render_template("index.html",dados = dados)

if __name__ == "__main__":
	app.run(debug=True)