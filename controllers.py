from flask import jsonify, request
from services import FilmeService
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

filme_service = FilmeService(os.getenv("BACKEND_SERVICES"))


def get_filmes():
    try:
        logger.info("Acessando o serviço de filmes")
        result = filme_service.get_filmes()
        logger.info("Serviço de filmes acessado com sucesso")
        return jsonify(result), 200
    except Exception as e:
        logger.error("Erro ao acessar o serviço de filmes: %s", e.response)
        return jsonify({"error": "Ocorreu um erro inesperado"}), 500


def get_filmes_favoritos():
    try:
        logger.info("Acessando o serviço de filmes favoritos")
        result = filme_service.get_filmes_favoritos()
        logger.info("Serviço de filmes favoritos acessado com sucesso")
        return jsonify(result), 200
    except Exception as e:
        logger.error("Erro ao acessar o serviço de filmes favoritos: %s", {e})
        return jsonify({"error": "Ocorreu um erro inesperado"}), 500


def create_filme():
    try:
        logger.info("Criando um novo filme")
        data = request.get_json()
        result = filme_service.create_filme(data)
        logger.info("Novo filme criado com sucesso")
        return jsonify(result), 201
    except Exception as e:
        logger.error("Erro ao criar o filme: %s", {e})
        return jsonify({"error": "Ocorreu um erro inesperado"}), 500


def replace_filme(filme_id):
    try:
        logger.info(f"Substituindo o filme com ID {filme_id}")
        data = request.get_json()
        result = filme_service.replace_filme(filme_id, data)
        logger.info(f"Filme com ID {filme_id} substituido com sucesso")
        return jsonify(result["value"]), 200
    except Exception as e:
        logger.error(f"Erro ao atualizar o filme com ID {filme_id}: {e}")
        return jsonify({"error": "Ocorreu um erro ao substituir o filme"}), 500


def update_filme(filme_id):
    try:
        logger.info(f"Atualizando parcialmente o filme com ID {filme_id}")
        data = request.get_json()
        result = filme_service.update_filme(filme_id, data)
        logger.info(f"Filme com ID {filme_id} atualizado parcialmente com sucesso")
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Erro ao atualizar parcialmente o filme com ID {filme_id}: {e}")
        return jsonify({"error": "Ocorreu um erro ao atualizar o filme"}), 500


def delete_filme(filme_id):
    try:
        logger.info(f"Excluindo o filme com ID {filme_id}")
        filme_service.delete_filme(filme_id)
        logger.info(f"Filme com ID {filme_id} excluído com sucesso")
        return jsonify({"message": "Filme excluído com sucesso"}), 200
    except Exception as e:
        logger.error(f"Erro ao excluir o filme com ID {filme_id}: {e}")
        return jsonify({"error": "Ocorreu um erro ao excluir o filme"}), 500


def register_routes(app):
    app.route("/filmes", methods=["GET"])(get_filmes)
    app.route("/filmes/favoritos", methods=["GET"])(get_filmes_favoritos)
    app.route("/filmes", methods=["POST"])(create_filme)
    app.route("/filmes/<int:filme_id>", methods=["PATCH"])(update_filme)
    app.route("/filmes/<int:filme_id>", methods=["PUT"])(replace_filme)
    app.route("/filmes/<int:filme_id>", methods=["DELETE"])(delete_filme)
