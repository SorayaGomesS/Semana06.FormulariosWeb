from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

dados_usuario = {
    "nome": None,
    "sobrenome": None,
    "instituicao": None,
    "disciplina": None
}

@app.route("/", methods=["GET", "POST"])
def home():
    global dados_usuario

    if request.method == "POST":
        dados_usuario["nome"] = request.form.get("nome")
        dados_usuario["sobrenome"] = request.form.get("sobrenome")
        dados_usuario["instituicao"] = request.form.get("instituicao")
        dados_usuario["disciplina"] = request.form.get("disciplina")

    return render_template("index.html", dados=dados_usuario)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        return redirect(url_for("acesso", usuario=usuario))
    return render_template("login.html")


@app.route("/acesso")
def acesso():
    usuario = request.args.get("usuario", "desconhecido")
    now = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template("acesso.html", usuario=usuario, now=now)


if __name__ == "__main__":
    app.run(debug=True)
