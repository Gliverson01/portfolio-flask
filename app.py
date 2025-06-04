from flask import Flask, render_template
import os

app = Flask(__name__, 
           template_folder=os.path.abspath('templates'),
           static_folder=os.path.abspath('static'))

# Dados de exemplo para os projetos
projetos = [
    {
        'id': 1,
        'nome': 'Sistema de Gerenciamento de Tarefas',
        'descricao': 'Aplicação web para gerenciamento de tarefas e projetos com funcionalidades de atribuição, prazos e notificações.',
        'tecnologias': ['Python', 'Django', 'PostgreSQL', 'Bootstrap', 'JavaScript'],
        'link': 'https://github.com/exemplo/gerenciador-tarefas'
    },
    {
        'id': 2,
        'nome': 'E-commerce de Produtos Artesanais',
        'descricao': 'Plataforma de comércio eletrônico para artesãos venderem seus produtos, com sistema de pagamento integrado e gestão de estoque.',
        'tecnologias': ['React', 'Node.js', 'MongoDB', 'Stripe API', 'AWS'],
        'link': 'https://github.com/exemplo/ecommerce-artesanato'
    },
    {
        'id': 3,
        'nome': 'Aplicativo de Monitoramento Fitness',
        'descricao': 'Aplicativo móvel para acompanhamento de atividades físicas, nutrição e metas de saúde, com visualização de dados e relatórios personalizados.',
        'tecnologias': ['Flutter', 'Firebase', 'Google Fit API', 'Charts.js', 'SQLite'],
        'link': 'https://github.com/exemplo/fitness-tracker'
    }
]

@app.route('/')
def index():
    return render_template('index.html', projetos=projetos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
