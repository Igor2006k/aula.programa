from flask import Flask, render_template
app = Flask(__name__)
def conexao():
    conn = sqlite3.connect('product.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def ola_mundo():
    return "Ola mundo"

@app.route('/home')
def home():
    conn = conexao()
    produto = conn.execute('SELECT * FROM product').fetchall()
    conn.close ()
    return redender_templates("index.html",)

if __name__ == "__main__":
app.run(debug=True)