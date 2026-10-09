# Base - Controle De Leituras

Esta é a aplicação-base da avaliação de reposição da turma 2V.

Ela já possui CRUD de leituras com SQLite, Blueprint de autenticação, Blueprint de leituras e uma função de segurança iniciada em `seguranca.py`. A autenticação com `session` e o controle de acesso por usuário ainda precisam ser implementados.

## Executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000`.

## Arquivos Principais

- `app.py`: cria a aplicação e registra os Blueprints.
- `auth.py`: rotas de cadastro, login e logout a serem completadas.
- `leituras.py`: rotas do CRUD de leituras.
- `seguranca.py`: função de proteção das rotas privadas.
- `database.py`: funções de banco de dados.
- `templates/`: páginas HTML.

## Observação

Não substitua a aplicação por outro projeto. A tarefa é adaptar esta base para autenticação com `session`, vinculando cada leitura ao usuário logado.



## JUSTIFICATIVAS


1. A separação utiliza os recursos de Blueprints que faz a modularização. isso traz beneficios como sepração das responsibilidades, é mais fácil para localizar códigos, adicionar coisas novas.

2. Por meio do objeto session, utiliza cookies criptografados. No login, ao validar as coisas do usuário com sucesso sistema traz um identificador único para aquele usuario. Aí em cada requisição o flask decodifica os cookies de sessão e disponibiliza o discionario, com a presença da chave session confirma que há um usuário autenticado, o valor indica qual é esse usuário.

3. Tem 3 camadas, a de autenticação: exigir login checa se tem um usuario id ativo, se não tiver usuário logado a requisição é interrompida e redireciona para a tela de login.
A camada de controle: rotas como listar, criar, buscar, atualizar, extraem o usuario id diretamente de session do usuário autenticado esse usuario id é obrigado a ser repassado para todas as camadas de funções de persistencia.
Camda de persistencia: Todas as coisas do SQL, impões uma condição obrigatória WHERE usuario_id = ?, mesmo que o usuário tente alterar a URL manualmente para acessar ou modificar Id de um livro que pertence a outro usuário, a consulta SQL não retornará nem afetará nenhum registro, garantindo isolamento total dos dados no banco de dados.
