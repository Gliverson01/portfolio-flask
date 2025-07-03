from flask import Flask, render_template, request, redirect, flash, url_for
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

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


def enviar_email(nome: str, email: str, assunto: str, mensagem: str) -> bool:
    """Envia um email utilizando configuracoes definidas em variaveis de ambiente."""
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    destinatario = os.getenv("CONTACT_EMAIL", smtp_username)

    if not smtp_server or not smtp_username or not smtp_password:
        app.logger.warning("SMTP nao configurado corretamente. Email nao enviado.")
        return False

    corpo = f"Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\n\n{mensagem}"

    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = destinatario
    msg["Subject"] = f"Contato do Portfolio: {assunto}"
    msg.attach(MIMEText(corpo, "plain"))

    contexto = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as servidor:
            servidor.starttls(context=contexto)
            servidor.login(smtp_username, smtp_password)
            servidor.sendmail(smtp_username, destinatario, msg.as_string())
        return True
    except Exception as e:  # pragma: no cover - envio de email nao testado
        app.logger.error("Erro ao enviar email: %s", e)
        return False

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

    if enviar_email(nome, email, assunto, mensagem):
        flash("Obrigado pelo contato! Responderei em breve.", "success")
    else:
        flash("Nao foi possivel enviar sua mensagem. Tente novamente mais tarde.", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
