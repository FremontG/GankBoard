from abc import ABC, abstractmethod
import requests
from .config import get_api_key, get_url  # Importer les fonctions pour récupérer la clé API et l'URL

class _GankBoardBaseObject(ABC):

    @classmethod
    def request(cls, method, endpoint, **kwargs):
        """Envoie une requête à l'API avec la clé API et l'URL stockées."""
        api_key = get_api_key()  # Récupérer la clé API définie globalement
        url = get_url()  # Récupérer l'URL de base

        headers = {'x-api-key': api_key}  # Utilisation de la clé API dans les en-têtes

        try:
            response = requests.request(method, f"{url}/{endpoint}", headers=headers, **kwargs)
            response.raise_for_status()  # Vérifie si la réponse a un code 2xx, sinon lève une erreur
            return response.json()  # Retourner la réponse en JSON si tout s'est bien passé
        except requests.exceptions.RequestException as e:
            return None, {'error': str(e)}
