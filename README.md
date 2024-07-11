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

- Inicie os serviços do Docker com Docker Compose:
Execute o arquivo docker-compose.yml no diretório raiz do projeto 

```
docker compose -f "docker-compose.yml" up -d --build
```

- Acesse a documentação da API:
Acesse o Swagger UI para visualizar e testar a API em http://localhost:5000/openapi/swagger.

