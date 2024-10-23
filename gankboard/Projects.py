import logging
from abstract import _GankBoardBaseObject

class ProjectObject(_GankBoardBaseObject):
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)

    def _build_project_data(self, name=None, description=None, **kwargs):
        """
        Construit les données JSON pour un projet.
        """
        data = {}
        
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        data.update(kwargs)
        return data

    def delete(self, resource_id):
        """
        Supprime un projet par son ID.
        """
        status_code, response = self.request(
            method="DELETE",
            endpoint=f"projects/{resource_id}"
        )

        if status_code != 204:
            error_message = (
                f"Échec de la suppression du rapport avec l'ID {resource_id}. "
                f"Code de statut: {status_code}. Détails de la réponse: {response}"
            )
            self.logger.error(error_message)  # Loguer l'erreur
            raise RuntimeError(error_message)  # Lever une exception avec le message d'erreur


        return status_code, response

    def modify(self, resource_id, name=None, description=None):
        """
        Modifie un projet existant par son ID.
        """
        status_code, response = self.request(
            method="PATCH",
            endpoint=f"projects/{resource_id}",
            json=self._build_project_data()
        )

        if status_code != 200:
            error_message = (
                f"Échec de la modification du rapport avec l'ID {resource_id}. "
                f"Code de statut: {status_code}. Détails de la réponse: {response}"
            )
            self.logger.error(error_message)  # Loguer l'erreur
            raise RuntimeError(error_message)  # Lever une exception avec le message d'erreur


        return status_code, response

    def create(self, name, description='', **kwargs):
        """
        Crée un nouveau projet.
        """
        status_code, response = self.request(
            method="POST",
            endpoint="projects",
            json=self._build_project_data(name=name, description=description, **kwargs)
        )

        if status_code != 201:
            error_message = (
                f"Échec de la création du rapport. Code de statut: {status_code}. "
                f"Détails de la réponse: {response}"
            )
            self.logger.error(error_message)  # Loguer l'erreur
            raise RuntimeError(error_message)

        return status_code, response
