from flask import Flask, render_template

app = Flask(__name__)

def connection():
    conn = sqlite3.connect(mateit.db)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = connection()
    dados = conn.execute("Select* from pessoa").fetchall()
    conn.close()
    render_template("index.html", dados = dados)

if __name__ == "__main__":
    app.run(debug=True)