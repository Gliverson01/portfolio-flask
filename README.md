# Portfolio Flask App

Este projeto é um portfólio simples desenvolvido com Flask.

## Como executar

1. Crie um ambiente virtual e instale as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Execute o servidor de desenvolvimento:

```bash
python app.py
```

A aplicação ficará disponível em `http://localhost:5000`.

## Variáveis de ambiente

- `SECRET_KEY`: chave para uso das mensagens *flash*.
- `PORT`: porta opcional para o servidor.
- `SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`: configuracoes do servidor SMTP para envio de emails do formulario de contato.
- `CONTACT_EMAIL`: endereco que recebera as mensagens enviadas pelo formulario (opcional, padrao usa `SMTP_USERNAME`).

## Estrutura

- `app.py`: aplicação Flask principal.
- `templates/`: arquivos HTML Jinja2.
- `static/`: arquivos de estilo.

Sinta-se livre para clonar e personalizar o portfólio conforme suas necessidades.
