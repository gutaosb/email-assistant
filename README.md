📧 Classificador Inteligente de Emails

Aplicação web que utiliza IA (NLP) para classificar emails em Produtivos ou Improdutivos, sugerindo automaticamente uma resposta adequada.

O objetivo é reduzir o trabalho manual de triagem de mensagens em empresas com grande volume de emails, liberando tempo da equipe para tarefas mais relevantes.

🚀 Demonstração Online

Frontend (React + Vite + Tailwind, hospedado no Vercel):

👉 https://email-assistant-nine.vercel.app

Backend (FastAPI, hospedado no Render):

👉 https://email-assistant-gsqb.onrender.com

⚠️ Observação: O backend no Render (plano gratuito) pode levar alguns segundos para “acordar” no primeiro acesso.

✨ Funcionalidades

Upload de arquivos .txt ou .pdf com emails

Inserção manual de texto do email

Classificação automática:

Produtivo → requer ação (solicitações, dúvidas, confirmações, etc.)

Improdutivo → não requer ação (felicitações, agradecimentos, etc.)

Sugestão automática de resposta baseada na categoria

Interface moderna, rápida e responsiva

🛠️ Tecnologias Utilizadas
Frontend:

React + Vite

TailwindCSS

Deploy: Vercel

Backend:

FastAPI

Hugging Face Inference API (modelo facebook/bart-large-mnli)

PyPDF2 (leitura de PDF)

Deploy: Render

⚙️ Como Rodar Localmente

🔹 Pré-requisitos

Python 3.10+

Node.js + npm

🔹 Clonar o repositório

git clone https://github.com/gutaosb/email-assistant.git

cd email-assistant

🔹 Backend

Entre na pasta do backend:

cd app/backend

Crie um ambiente virtual e instale dependências:

python -m venv venv

source venv/bin/activate # Linux/Mac

venv\Scripts\activate # Windows

pip install -r requirements.txt

Configure variáveis de ambiente:

Crie o arquivo .env na pasta backend:

HF_API_TOKEN=seu_token_da_huggingface

Rode o servidor:

uvicorn main:app --reload

👉 disponível em http://127.0.0.1:8000

🔹 Frontend

Entre na pasta do frontend:

cd app/frontend

Instale as dependências:

npm install

Configure o .env baseado no .env.example:

VITE_API_URL=http://127.0.0.1:8000

Rode a aplicação:

npm run dev

👉 disponível em http://localhost:5173

🧪 Exemplos de Emails para Teste

✅ Produtivo
Olá equipe, gostaria de saber qual é o status da minha solicitação de acesso ao sistema financeiro. Preciso dessa liberação até sexta-feira.

❌ Improdutivo
Olá, tudo bem? Quero desejar um ótimo final de semana a toda a equipe!

📂 Estrutura do Projeto
app/
| backend/
| ├── main.py # API FastAPI
| ├── services.py # Classificação e resposta automática
| ├── utils.py # Funções auxiliares (leitura PDF, normalização texto)
| ├── requirements.txt
| ├── .env
|
| frontend/
| ├── src/
| │ ├── App.jsx
| │ ├── main.jsx
| │ ├── components/
| ├── package.json
| ├── vite.config.js
| ├── .env

👨‍💻 Autor

Feito por Augusto Semensato Bortoloti

LinkedIn: linkedin.com/in/augustosb

GitHub: github.com/gutaosb
