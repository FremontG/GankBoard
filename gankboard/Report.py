import logging
from ._GankBoardBaseObject import _GankBoardBaseObject

class Report(_GankBoardBaseObject):
    
    def _build_report_data(self, project_id, observation, date=None):
        """
        Construit les données JSON pour un rapport.
        """
        data = {}
        
        if project_id is not None:
            data["project"] = project_id
        if observation is not None:
            data["observation"] = observation
        if date is not None:
            data["date"] = date
        return data

    @classmethod
    def delete(cls, resource_id):
        """
        Supprime un rapport par son ID en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête DELETE pour le rapport avec l'ID {resource_id}")
        response = cls.request(
            method="DELETE",
            endpoint=f"reports/{resource_id}/"
        )

        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la suppression du rapport avec l'ID {resource_id}: {error_message}")
            raise RuntimeError(f"Erreur lors de la suppression du rapport avec l'ID {resource_id}: {error_message}")

        logging.info(f"Rapport avec l'ID {resource_id} supprimé avec succès.")
        return response

    @classmethod
    def modify(cls, resource_id, project_id=None, observation=None, date=None):
        """
        Modifie un rapport existant par son ID en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête PATCH pour modifier le rapport avec l'ID {resource_id}")
        response = cls.request(
            method="PATCH",
            endpoint=f"reports/{resource_id}/",
            json=cls()._build_report_data(project_id=project_id, observation=observation, date=date)
        )

        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la modification du rapport avec l'ID {resource_id}: {error_message}")
            raise RuntimeError(f"Erreur lors de la modification du rapport avec l'ID {resource_id}: {error_message}")

        logging.info(f"Rapport avec l'ID {resource_id} modifié avec succès.")
        return response

    @classmethod
    def create(cls, project_id, observation='', date=None):
        """
        Crée un nouveau rapport en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête POST pour créer un nouveau rapport")
        response = cls.request(
            method="POST",
            endpoint="reports/",
            json=cls()._build_report_data(project_id=project_id, observation=observation, date=date)
        )

        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la création du rapport: {error_message}")
            raise RuntimeError(f"Erreur lors de la création du rapport: {error_message}")

        logging.info(f"Rapport pour le projet '{project_id}' créé avec succès.")
        return response
