from flask import Flask, render_template, request
from datetime import datetime
import socket

app = Flask(__name__)

# ---------------- Home ----------------
@app.route("/", methods=["GET", "POST"])
def home():
    nome = "Estranho"
    instituicao = None
    disciplina = None
    ip_remoto = None
    host_app = None

    if request.method == "POST":
        nome = request.form.get("nome", "Estranho")
        instituicao = request.form.get("instituicao")
        disciplina = request.form.get("disciplina")
        ip_remoto = request.remote_addr
        host_app = socket.gethostname()

    return render_template(
        "index.html",
        nome=nome,
        instituicao=instituicao,
        disciplina=disciplina,
        ip_remoto=ip_remoto,
        host_app=host_app,
    )

# ---------------- Login ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    usuario = None
    data_hora_atual = None
    data_hora_passada = None

    if request.method == "POST":
        usuario = request.form.get("usuario")
        data_hora_atual = datetime.now().strftime("%B %d, %Y %I:%M %p")
        data_hora_passada = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")

    return render_template(
        "login.html",
        usuario=usuario,
        data_hora_atual=data_hora_atual,
        data_hora_passada=data_hora_passada,
    )

if __name__ == "__main__":
    app.run(debug=True)
