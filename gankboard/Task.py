import logging
from ._GankBoardBaseObject import _GankBoardBaseObject

class Task(_GankBoardBaseObject):

    def _build_task_data(self, project_id, name, description=None, dependencies=None, parent_task=None, sub_tasks=None, **kwargs):
        """
        Construit les données JSON pour une tâche.
        """
        data = {}

        if project_id is not None:
            data["project"] = project_id
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if dependencies is not None:
            data["dependencies"] = dependencies
        else:
            data["dependencies"] = []  # Valeur par défaut si non spécifiée
        if parent_task is not None:
            data["parent_task"] = parent_task
        if sub_tasks is not None:
            data["sub_tasks"] = sub_tasks
        else:
            data["sub_tasks"] = []  # Valeur par défaut si non spécifiée
        
        data.update(kwargs)
        return data

    @classmethod
    def delete(cls, resource_id):
        """
        Supprime une tâche par son ID en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête DELETE pour la tâche avec l'ID {resource_id}")
        response = cls.request(
            method="DELETE",
            endpoint=f"tasks/{resource_id}/"
        )

        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la suppression de la tâche avec l'ID {resource_id}: {error_message}")
            raise RuntimeError(f"Erreur lors de la suppression de la tâche avec l'ID {resource_id}: {error_message}")

        logging.info(f"Tâche avec l'ID {resource_id} supprimée avec succès.")
        return response

    @classmethod
    def modify(cls, resource_id, project_id, name, description='', dependencies=None, parent_task=None, sub_tasks=None, **kwargs):
        """
        Modifie une tâche existante par son ID en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête PATCH pour modifier la tâche avec l'ID {resource_id}")
        response = cls.request(
            method="PATCH",
            endpoint=f"tasks/{resource_id}/",
            json=cls()._build_task_data(project_id=project_id, name=name, description=description, dependencies=dependencies, parent_task=parent_task, sub_tasks=sub_tasks, **kwargs)
        )

        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la modification de la tâche avec l'ID {resource_id}: {error_message}")
            raise RuntimeError(f"Erreur lors de la modification de la tâche avec l'ID {resource_id}: {error_message}")

        logging.info(f"Tâche avec l'ID {resource_id} modifiée avec succès.")
        return response

    @classmethod
    def create(cls, project_id, name, description='', dependencies=None, parent_task=None, sub_tasks=None, **kwargs):
        """
        Crée une nouvelle tâche en utilisant la clé API globale.
        """
        logging.info(f"Envoi d'une requête POST pour créer une nouvelle tâche : {name}")
        response = cls.request(
            method="POST",
            endpoint="tasks/",
            json=cls()._build_task_data(project_id=project_id, name=name, description=description, dependencies=dependencies, parent_task=parent_task, sub_tasks=sub_tasks, **kwargs)
        )

        if response is None or 'error' in response:
            error_message = response.get('error', 'Erreur inconnue')
            logging.error(f"Erreur lors de la création de la tâche : {error_message}")
            raise RuntimeError(f"Erreur lors de la création de la tâche : {error_message}")

        logging.info(f"Tâche '{name}' créée avec succès.")
        return response
