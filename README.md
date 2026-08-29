# API de Gestão de Entregas & Consulta Climática (Django REST Framework)

Aplicação backend desenvolvida em Django REST Framework (DRF) para gestão de entregadores, motos e consulta unificada de localização (via BrasilAPI) e condições climáticas (via WeatherAPI), com registro histórico de consultas.

---

## ?? Funcionalidades

- **CRUD de Entregadores**: Cadastro e gerenciamento de entregadores.
- **CRUD de Motos**: Cadastro e gerenciamento de veículos vinculados aos entregadores.
- **Consulta Unificada (CEP + Clima)**: Endpoint que consulta dados de endereço e temperatura atual da cidade.
- **Histórico de Consultas**: Armazenamento automático no banco de dados de todas as cidades e CEPs pesquisados.

---

## ?? Pré-requisitos

Certifique-se de ter instalado em sua máquina:
- Python (versão 3.10 ou superior)
- Git

---

## ?? Passo a Passo para Executar o Projeto

Siga os passos abaixo no seu terminal para rodar o projeto localmente:

### 1. Clonar o Repositório
\\\ash
git clone https://github.com/paulohf07/wsBackendFabricaDeSoftware26.2.git
cd wsBackendFabricaDeSoftware26.2
\\\

### 2. Criar e Ativar o Ambiente Virtual (\env\)
Crie o ambiente virtual na pasta do projeto:
\\\ash
python -m venv venv
\\\

Ative o ambiente virtual:
- **No Windows (PowerShell):**
  \\\powershell
  .\venv\Scripts\Activate.ps1
  \\\
- **No Windows (CMD):**
  \\\cmd
  venv\Scripts\activate.bat
  \\\
- **No Linux / macOS:**
  \\\ash
  source venv/bin/activate
  \\\

### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale os pacotes necessários:
\\\ash
pip install -r requirements.txt
\\\

### 4. Aplicar as Migrações do Banco de Dados
Configure as tabelas no banco de dados local:
\\\ash
python manage.py makemigrations
python manage.py migrate
\\\

### 5. Iniciar o Servidor Local
Execute o servidor de desenvolvimento do Django:
\\\ash
python manage.py runserver
\\\

---

## ?? Como Testar a API

Com o servidor rodando (\http://127.0.0.1:8000/\), você pode acessar as seguintes rotas:

- **Raiz da API**: \http://127.0.0.1:8000/\
- **Gerenciar Entregadores (CRUD)**: \http://127.0.0.1:8000/entregadores/\
- **Gerenciar Motos (CRUD)**: \http://127.0.0.1:8000/motos/\
- **Consultar CEP e Clima**: \http://127.0.0.1:8000/consultar-entrega/?cep=55880000\
- **Visualizar Histórico**: \http://127.0.0.1:8000/historico/\
- **Painel Administrativo**: \http://127.0.0.1:8000/admin/\

