import logging
from ._GankBoardBaseObject import _GankBoardBaseObject

class Project(_GankBoardBaseObject):

    def _build_project_data(self, name=None, description=None):
        """
        Construit les données JSON pour un projet.
        """
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        return data

    @classmethod
    def delete(cls, resource_id):
        """
        Supprime un projet par son ID en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête DELETE pour le projet avec l'ID {resource_id}")
        response = cls.request(
            method="DELETE",
            endpoint=f"projects/{resource_id}"
        )

        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la suppression du projet avec l'ID {resource_id}: {error_message}")
            raise RuntimeError(f"Erreur lors de la suppression du projet avec l'ID {resource_id}: {error_message}")

        logging.info(f"Projet avec l'ID {resource_id} supprimé avec succès.")
        return response

    @classmethod
    def modify(cls, resource_id, name=None, description=None, **kwargs):
        """
        Modifie un projet existant par son ID en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête PATCH pour modifier le projet avec l'ID {resource_id}")
        response = cls.request(
            method="PATCH",
            endpoint=f"projects/{resource_id}/",
            json=cls()._build_project_data(name=name, description=description, **kwargs)
        )

        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la modification du projet avec l'ID {resource_id}: {error_message}")
            raise RuntimeError(f"Erreur lors de la modification du projet avec l'ID {resource_id}: {error_message}")

        logging.info(f"Projet avec l'ID {resource_id} modifié avec succès.")
        return response

    @classmethod
    def create(cls, name, description='', **kwargs):
        """
        Crée un nouveau projet en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête POST pour créer un nouveau projet : {name}")
        response = cls.request(
            method="POST",
            endpoint="projects/",
            json=cls()._build_project_data(name=name, description=description, **kwargs)
        )
        print(response)
        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la création du projet : {error_message}")
            raise RuntimeError(f"Erreur lors de la création du projet : {error_message}")

        logging.info(f"Projet '{name}' créé avec succès.")
        return response
