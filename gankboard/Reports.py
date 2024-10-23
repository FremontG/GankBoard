import logging
from abstract import _GankBoardBaseObject

class ReportObject(_GankBoardBaseObject):
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)

    def _build_report_data(self, project_id=None, observation=None, **kwargs):
        """
        Construit les données JSON pour un rapport.
        """
        data = {}
        
        if project_id is not None:
            data["project"] = project_id
        if observation is not None:
            data["observation"] = observation
        data.update(kwargs)
        return data

    def delete(self, resource_id):
        """
        Supprime un rapport par son ID.
        """
        status_code, response = self.request(
            method="DELETE",
            endpoint=f"reports/{resource_id}"
        )

        if status_code != 204:
            error_message = (
                f"Échec de la suppression du rapport avec l'ID {resource_id}. "
                f"Code de statut: {status_code}. Détails de la réponse: {response}"
            )
            self.logger.error(error_message)  # Loguer l'erreur
            raise RuntimeError(error_message)  # Lever une exception avec le message d'erreur


        return status_code, response

    def modify(self, resource_id, project_id=None, observation=None):
        """
        Modifie un rapport existant par son ID.
        """
        status_code, response = self.request(
            method="PATCH",
            endpoint=f"reports/{resource_id}",
            json=self._build_report_data()
        )

        if status_code != 200:
            error_message = (
                f"Échec de la modification du rapport avec l'ID {resource_id}. "
                f"Code de statut: {status_code}. Détails de la réponse: {response}"
            )
            self.logger.error(error_message)  # Loguer l'erreur
            raise RuntimeError(error_message)  # Lever une exception avec le message d'erreur


        return status_code, response

    def create(self, project_id, observation='', **kwargs):
        """
        Crée un nouveau rapport.
        """
        status_code, response = self.request(
            method="POST",
            endpoint="reports",
            json=self._build_report_data(project_id=project_id, observation=observation, **kwargs)
        )

        if status_code != 201:
            error_message = (
                f"Échec de la création du rapport. Code de statut: {status_code}. "
                f"Détails de la réponse: {response}"
            )
            self.logger.error(error_message)  # Loguer l'erreur
            raise RuntimeError(error_message)
        return status_code, response
