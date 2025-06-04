from flask import Flask, render_template
import os

app = Flask(__name__,
            template_folder=os.path.abspath('templates'),
            static_folder=os.path.abspath('static'))

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
    return render_template('index.html', projetos=projetos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
