# API de Controle de Disciplinas e Tarefas de Aluno

Esta é uma API desenvolvida em Django para ajudar os alunos a gerenciarem suas disciplinas e tarefas. A API fornece uma série de endpoints para realizar operações CRUD (Create, Read, Update, Delete) em alunos, disciplinas e tarefas, bem como consultas relacionadas a esses recursos.

# Modelos de Dados

A API possui três modelos principais:
Aluno;
Disciplinas;
Tarefa;

# Métodos da Api

Todos os modelos possuem Get, Post, PUT e Delete para que o usúario possa listar, visualizar um item em específico,
atualizar e deletar.

# Como Rodar a API

- Criar um ambiente virtualizado
  python -m venv .env
- Ativar
  .\.env\Scripts\activate
- Instalar dependecias
  pip install -r requirements.txt
- startar a aaplicação:
  python manage.py runserver

Não esquecer de fazer as migrações

# Exemplos de requisição pelo POSTMAN

No arquivo AlunoDjango.postman_collection existe alguns exemplos utilizando a rotas da api, como por exemplo:

Url: http://127.0.0.1:8000/tarefas/1/update/ Método PUT

Exemplo de Body(json):

{
"id": 1,
"titulo": "Modifiquei",
"descricao": "Esta é uma tarefa de exemplo.",
"data_entrega": "2023-12-31",
"concluida": false,
"aluno": 4,
"disciplinas": [
4
]
}
