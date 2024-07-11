from flask import jsonify
from schemas.filmeSchema import Filme, FilmeId, FilmeList, FilmeUpdateParcial
from services.services import FilmeService
from flask_openapi3 import Tag, APIBlueprint
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api = APIBlueprint("api", __name__, url_prefix="/api")

filme_service = FilmeService(os.getenv("BACKEND_SERVICES"))
filme_tag = Tag(name="Filme", description="Operações relacionadas a filmes")


@api.get(
    "/filmes",
    tags=[filme_tag],
    responses={"200": FilmeList, "500": {"description": "Erro interno do servidor"}},
)
def get_filmes():
    try:
        logger.info("Acessando o serviço de filmes")
        result = filme_service.get_filmes()
        filmes = [Filme(**filme) for filme in result]
        filme_list = FilmeList(filmes=filmes)
        logger.info("Serviço de filmes acessado com sucesso")
        return jsonify(filme_list.model_dump()), 200
    except Exception as e:
        logger.error("Erro ao acessar o serviço de filmes: %s", e.response)
        return jsonify({"error": "Ocorreu um erro inesperado"}), 500


@api.get(
    "/filmes/favoritos",
    tags=[filme_tag],
    responses={"200": FilmeList, "500": {"description": "Erro interno do servidor"}},
)
def get_filmes_favoritos():
    try:
        logger.info("Acessando o serviço de filmes favoritos")
        result = filme_service.get_filmes_favoritos()
        filmes = [Filme(**filme) for filme in result]
        filme_list = FilmeList(filmes=filmes)
        logger.info("Serviço de filmes favoritos acessado com sucesso")
        return jsonify(filme_list.model_dump()), 200
    except Exception as e:
        logger.error("Erro ao acessar o serviço de filmes favoritos: %s", {e})
        return jsonify({"error": "Ocorreu um erro inesperado"}), 500


@api.post(
    "/filmes",
    tags=[filme_tag],
    description="Cria um novo filme com os dados fornecidos",
    responses={
        "201": Filme,
        "400": {"description": "Dados inválidos"},
        "500": {"description": "Erro interno do servidor"},
    },
)
def create_filme(body: Filme):
    try:
        logger.info("Criando um novo filme")
        filme_data = body.model_dump()
        result = filme_service.create_filme(filme_data)
        logger.info("Novo filme criado com sucesso")
        return jsonify(Filme(**result).model_dump()), 201
    except Exception as e:
        logger.error("Erro ao criar o filme: %s", {e})
        return jsonify({"error": "Ocorreu um erro inesperado"}), 500


@api.put(
    "/filmes/<int:filme_id>",
    tags=[filme_tag],
    responses={
        "200": Filme,
        "400": {"description": "Dados inválidos"},
        "500": {"description": "Erro interno do servidor"},
    },
)
def replace_filme(path: FilmeId, body: Filme):
    try:
        filme_id = path.filme_id
        logger.info(f"Substituindo o filme com ID {filme_id}")
        filme_data = body.model_dump()
        result = filme_service.replace_filme(filme_id, filme_data)
        logger.info(f"Filme com ID {filme_id} substituído com sucesso")
        return jsonify(Filme(**result["value"]).model_dump()), 200
    except Exception as e:
        logger.error(f"Erro ao atualizar o filme com ID {filme_id}: {e}")
        return jsonify({"error": "Ocorreu um erro ao substituir o filme"}), 500


@api.patch(
    "/filmes/<int:filme_id>",
    tags=[filme_tag],
    responses={
        "200": Filme,
        "400": {"description": "Dados inválidos"},
        "500": {"description": "Erro interno do servidor"},
    },
)
def update_filme(path: FilmeId, body: FilmeUpdateParcial):
    try:
        filme_id = path.filme_id
        logger.info(f"Atualizando o filme com ID {filme_id}")
        filme_data = body.model_dump()
        result = filme_service.update_filme(filme_id, filme_data)
        logger.info(f"Filme com ID {filme_id} atualizado com sucesso")
        return jsonify(result["value"]), 200
    except Exception as e:
        logger.error(f"Erro ao atualizar parcialmente o filme com ID {filme_id}: {e}")
        return jsonify({"error": "Ocorreu um erro ao atualizar o filme"}), 500


@api.delete(
    "/filmes/<int:filme_id>",
    tags=[filme_tag],
    responses={
        "200": {"message": "Filme excluído com sucesso"},
        "500": {"description": "Erro interno do servidor"},
    },
)
def delete_filme(path: FilmeId):
    try:
        filme_id = path.filme_id
        logger.info(f"Excluindo o filme com ID {filme_id}")
        filme_service.delete_filme(filme_id)
        logger.info(f"Filme com ID {filme_id} excluído com sucesso")
        return jsonify({"message": "Filme excluído com sucesso"}), 200
    except Exception as e:
        logger.error(f"Erro ao excluir o filme com ID {filme_id}: {e}")
        return jsonify({"error": "Ocorreu um erro ao excluir o filme"}), 500
