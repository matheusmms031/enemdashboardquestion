# Galaxy Enem Dashboard

Projeto: Dashboard interativo com questões do ENEM, filtrável e analisável.

Esta aplicação fornece uma interface para explorar todas as questões do ENEM, com classificação e filtros por:

- Dificuldade (extraída dos metadados)
- Habilidades (Matriz do ENEM)
- Competências (Matriz do ENEM)

## Visão Geral

O objetivo do projeto é disponibilizar um dashboard amigável que permita professores, estudantes e pesquisadores:

- analisar a distribuição de questões por dificuldade;
- navegar por habilidades e competências associadas;
- filtrar questões por tópicos e metadados;
- exportar ou consultar os dados via API.

## Arquitetura

O sistema é dividido em duas partes principais:

- Frontend: aplicação em `React.js` para a interface do usuário (dashboard, filtros, visualizações).
- Backend: API REST feita em `Flask` (Python) que expõe endpoints para consulta de questões e estatísticas.
- Banco de dados: `MongoDB` (NoSQL) para armazenar as questões e metadados.

## Tecnologias

- **Frontend:** React.js, ferramentas típicas (`npm`/`yarn`, Vite ou Create React App opcional).
- **Backend:** Python 3.x, Flask, PyMongo (ou motor async alternativo como Motor).
- **Banco de Dados:** MongoDB (local ou em nuvem — Atlas).

## Estrutura do Repositório

- `dbenem.json` : dump ou amostra das questões (formato JSON) usadas para alimentar o banco.
- `lista_topicos.json` : mapeamento/estrutura de tópicos usado pelo dashboard.
- `README.md` : este arquivo.
- `LICENSE` : licença do projeto.

## Pré-requisitos

- `node` e `npm`/`yarn` para o frontend.
- `python` 3.10+ e `pip` para o backend.
- Uma instância do MongoDB (local ou Atlas).

## Como executar (desenvolvimento)

### Backend (Flask)

1. Criar e ativar virtualenv:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependências (exemplo):

```bash
pip install flask pymongo python-dotenv
```

3. Variáveis de ambiente necessárias (exemplo):

```bash
export MONGO_URI="mongodb://localhost:27017/enem"
export FLASK_APP=app.py
export FLASK_ENV=development
```

4. Rodar a API:

```bash
flask run --host=0.0.0.0 --port=5000
```

### Frontend (React)

1. Entrar na pasta do frontend (quando existir) e instalar dependências:

```bash
cd frontend
npm install
```

2. Rodar em modo desenvolvimento:

```bash
npm run dev
# ou
npm start
```

## Conexão com MongoDB

- Importar `dbenem.json` para o MongoDB (exemplo com `mongoimport`):

```bash
mongoimport --uri "$MONGO_URI" --collection questões --file dbenem.json --jsonArray
```

- A coleção sugerida: `questoes`.

## Formato dos dados

- `dbenem.json` deve ser um array de objetos JSON com campos como `id`, `enunciado`, `alternativas`, `dificuldade`, `habilidades`, `competencias`, `topicos` e outros metadados.
- `lista_topicos.json` deve conter a lista hierárquica de tópicos usada para filtros e agrupamentos.

## Exemplos de endpoints (sugestão)

- `GET /api/questoes` : lista de questões (aceita filtros por dificuldade, habilidade, competência, tópico).
- `GET /api/questoes/:id` : detalhe de uma questão.
- `GET /api/stats/dificuldade` : estatísticas por dificuldade.
- `GET /api/stats/habilidade` : estatísticas por habilidade.

Exemplo de consulta com query params:

```
GET /api/questoes?dificuldade=media&habilidade=H12&topico=funcoes
```

## Boas práticas e recomendações

- Indice as coleções no MongoDB para campos usados em filtros (`dificuldade`, `habilidades`, `topicos`) para melhorar performance.
- Paginação: implemente paginação para `GET /api/questoes` (limit/offset ou cursor-based).
- Autenticação (opcional): proteger endpoints administrativos se o dashboard tiver painéis privados.

## Como contribuir

- Abra issues para bugs e features.
- Envie PRs com uma descrição clara do que foi alterado.
- Adicione testes (unitários/integrados) para funcionalidades críticas.

## Licença

O projeto inclui um arquivo `LICENSE` na raiz — verifique o tipo de licença adotada.

## Próximos passos sugeridos

- Criar scaffold do backend em `backend/` com `app.py`, rotas básicas e `requirements.txt`.
- Criar scaffold do frontend em `frontend/` com `package.json` e estrutura de páginas do dashboard.
- Adicionar scripts de importação para popular o MongoDB a partir de `dbenem.json`.

Se quiser, eu posso gerar o scaffold inicial do backend (Flask) e do frontend (React) agora.