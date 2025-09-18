from flask import Flask, render_template, request

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
        senha = request.form.get("senha")
        return f"Usuário {usuario} tentou logar!"

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
