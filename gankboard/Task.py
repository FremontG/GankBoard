from abstract import _GankBoardBaseObject

class Task(_GankBoardBaseObject):
    
    def __init__(self, api_key):
        self.api_key = api_key

    def _build_task_data(project_id=None, name=None, description=None, dependencies=None, parent_task=None, sub_tasks=None, **kwargs):
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


    def delete(self, resource_id):
        """
        Supprime une tâche par son ID.
        """
        status_code, response = self.request(
            method="DELETE",
            endpoint=f"tasks/{resource_id}"
        )

        return status_code, response

    def modify(self, resource_id, project_id, name, description='', dependencies=None, parent_task=None, sub_tasks=None, **kwargs):
        """
        Modifie une tâche existante par son ID.
        """
        status_code, response = self.request(
            method="PATCH",
            endpoint=f"tasks/{resource_id}",
            json=self._build_task_data(project_id, name, description, dependencies, parent_task, sub_tasks, **kwargs)
        )

        return status_code, response

    def create(self, project_id, name, description='', dependencies=None, parent_task=None, sub_tasks=None, **kwargs):
        """
        Crée une nouvelle tâche.
        """
        status_code, response = self.request(
            method="POST",
            endpoint="tasks",
            json=self._build_task_data(project_id, name, description, dependencies, parent_task, sub_tasks, **kwargs)
        )

        return status_code, response
