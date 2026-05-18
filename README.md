# pos_fast_api
Desenvolvimento em Python com FastApi

# Repositório com código fonte da disciplina de API

## Criação do arquivo .env

Faça uma cópia do arquivo `.env.sample` e coloque com o nome `.env` e preencha as variáveis

## Instalação de dependências (bibliotecas)

```bash
uv sync
```

## Executar a aplicação localmente

```bash
uvicorn main:app --reload
```

Caso já esteja com o ambiente virtual ativado:
```bash
.\.venv\Scripts\activate
uvicorn main:app --reload
```

A aplicação estará disponível em: http://localhost:8000

A documentação interativa (Swagger UI) estará em: http://localhost:8000/docs

## Configuração do projeto do zero (Comandos utilizados)

Caso você precise recriar o projeto do zero, aqui estão os comandos utilizados passo a passo:

```bash
pip install uv
uv init 
uv add "fastapi[standard]" 
.\.venv\Scripts\activate
uv add uvicorn
uvicorn main:app --reload
```
