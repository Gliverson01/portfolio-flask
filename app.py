from flask import Flask, render_template, request, redirect, flash, url_for
import os
from datetime import datetime

app = Flask(
    __name__,
    template_folder=os.path.abspath("templates"),
    static_folder=os.path.abspath("static"),
)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-secret")

# Projetos reais com base no seu currículo
projetos = [
    {
        'id': 1,
        'nome': 'Automação de Rotinas com Ansible e Docker',
        'descricao': 'Scripts e playbooks criados para automatizar rotinas críticas de servidores, reduzindo em 30% o tempo de execução.',
        'tecnologias': ['Ansible', 'Docker', 'Python', 'Shell Script'],
        'link': 'https://github.com/gliversonfrp/infra-automation'  # ajuste conforme seu GitHub real
    },
    {
        'id': 2,
        'nome': 'Monitoramento com Prometheus e Grafana',
        'descricao': 'Dashboard de monitoramento implementado em servidores cloud com foco em performance e custo.',
        'tecnologias': ['Prometheus', 'Grafana', 'Linux', 'AWS'],
        'link': 'https://github.com/gliversonfrp/server-monitoring'
    },
    {
        'id': 3,
        'nome': 'Provisionamento com Terraform',
        'descricao': 'Infraestrutura criada como código para ambientes cloud escaláveis, utilizando AWS e DigitalOcean.',
        'tecnologias': ['Terraform', 'AWS', 'DigitalOcean', 'IaC'],
        'link': 'https://github.com/gliversonfrp/cloud-provisioning'
    }
]

@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template("index.html", projetos=projetos, current_year=current_year)


@app.route("/contato", methods=["POST"])
def contato():
    nome = request.form.get("nome")
    email = request.form.get("email")
    assunto = request.form.get("assunto")
    mensagem = request.form.get("mensagem")

    app.logger.info("Mensagem recebida de %s <%s>: %s", nome, email, assunto)

    flash("Obrigado pelo contato! Responderei em breve.", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
