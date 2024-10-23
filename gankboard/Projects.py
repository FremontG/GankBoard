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

        return status_code, response
