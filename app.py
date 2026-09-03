import os

from flask import Flask, render_template

app = Flask(__name__)

# Banco de dados provisório. Será substituído nas próximas etapas do projeto.
chamados = [
    {"id": 1, "titulo": "Impressora do 2º andar não liga", "status": "aberto"},
    {"id": 2, "titulo": "Sistema de vendas lento", "status": "em andamento"},
    {"id": 3, "titulo": "Solicitação de acesso ao ERP", "status": "resolvido"},
]

equipe = [
    {
        "nome": "Max Iago Villafan",
        "papel": "Product Owner / CIO, Dev Lead e QA / Auditoria",
    },
]

@app.route("/")
def index():
    return render_template("index.html", chamados=chamados, total=len(chamados))

@app.route("/sobre")
def sobre():
    return render_template("sobre.html", equipe=equipe)

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=porta, debug=True)
