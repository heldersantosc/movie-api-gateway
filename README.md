# API Gateway de Catálogo de Filmes
Esta API Gateway serve como ponto de entrada para o serviço de catálogo de filmes, gerenciando requisições e roteando-as para os microserviços apropriados.

## Instruções de Instalação
Siga as etapas abaixo para configurar o ambiente local e iniciar a aplicação.

### Pré-requisitos

- Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Docker e Docker Compose (para execução em contêineres)


### Passo a Passo

**Clone o repositório:**

```
git clone https://github.com/heldersantosc/movie-api-gateway.git
cd movie-api-gateway
```

### 1.1. Para executar localmente ###
**Crie um ambiente virtual:**
```
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

**Instale as dependências:**
```
pip install -r requirements.txt
```

**Execute a aplicação:**
```
python app.py

ou

python3 app.py
```


### 1.2. Para executar com o docker ###
**Construa e inicie os contêineres:**
```
docker-compose up --build
```