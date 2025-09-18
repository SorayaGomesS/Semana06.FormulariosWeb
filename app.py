from flask import Flask, render_template, request
from datetime import datetime
import socket

app = Flask(__name__)

user_data = {
    "nome": "Estranho",
    "instituicao": None,
    "disciplina": None,
    "ip": None,
    "host": None
}


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_data["nome"] = request.form.get("nome", "Estranho")
        user_data["instituicao"] = request.form.get("instituicao", None)
        user_data["disciplina"] = request.form.get("disciplina", None)
        user_data["ip"] = request.remote_addr
        user_data["host"] = socket.gethostname()

    return render_template("home.html", user=user_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    username = None
    local_time = None

    if request.method == "POST":
        username = request.form.get("username")
        local_time = datetime.now().strftime("%B %d, %Y %I:%M %p")

    return render_template("login.html", username=username, local_time=local_time)


if __name__ == "__main__":
    app.run(debug=True)

