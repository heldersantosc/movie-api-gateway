from requests import get, post, patch, delete, put
import logging

logger = logging.getLogger(__name__)


class FilmeService:
    def __init__(self, backend_url):
        self.backend_url = backend_url
        logger.info(backend_url)

    def get_filmes(self):
        response = get(f"{self.backend_url}/filmes")
        response.raise_for_status()
        return response.json()

    def get_filmes_favoritos(self):
        response = get(f"{self.backend_url}/filmes/favoritos")
        response.raise_for_status()
        return response.json()

    def create_filme(self, data):
        response = post(f"{self.backend_url}/filmes", json=data)
        response.raise_for_status()
        return response.json()

    def replace_filme(self, filme_id, data):
        response = put(f"{self.backend_url}/filmes/{filme_id}", json=data)
        response.raise_for_status()
        return response.json()

    def update_filme(self, filme_id, data):
        response = patch(f"{self.backend_url}/filmes/{filme_id}", json=data)
        response.raise_for_status()
        return response.json()

    def delete_filme(self, filme_id):
        response = delete(f"{self.backend_url}/filmes/{filme_id}")
        response.raise_for_status()
