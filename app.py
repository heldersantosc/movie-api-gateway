from flask_openapi3 import OpenAPI, Info
from controllers.controllers import api as api_blueprint
from dotenv import load_dotenv
import os

load_dotenv()

info = Info(title="API Gateway de Catálogo de Filmes", version="1.0.0")

port = os.getenv("PORT")

app = OpenAPI(__name__, info=info)
app.register_api(api_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
