# Portfolio Flask App

Este é um pequeno projeto de portfólio desenvolvido com Flask. Ele apresenta alguns dos meus projetos e disponibiliza um formulário de contato.

## Configuração

1. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Defina as variáveis de ambiente opcionais:
   - `SECRET_KEY` – chave secreta do Flask
   - `PORT` – porta para executar a aplicação (padrão: 5000)

## Executando

```
python app.py
```
A aplicação ficará disponível em `http://localhost:PORT`.

## Estrutura

- `app.py` – aplicação Flask
- `templates/` – arquivos HTML
- `static/` – CSS e outros arquivos estáticos
- `wsgi.py` – ponto de entrada para servidores WSGI

Sinta‑se à vontade para customizar e ampliar este projeto.
