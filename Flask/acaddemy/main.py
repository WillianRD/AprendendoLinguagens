from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "Gestão de Pessoas"
    usuarios = [
        {"nome": "Willian" , "membro_ativo": True},
        {"nome": "Coda Fofo" , "membro_ativo": False},
        {"nome": "Yuri" , "membro_ativo": False},
        {"nome": "Teste", "membro_ativo":True},
    ]
    return render_template("index.html", titulo = titulo, usuarios = usuarios)

@app.route('/sobre')
def sobre():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)

