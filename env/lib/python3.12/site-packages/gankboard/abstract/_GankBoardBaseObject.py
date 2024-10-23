from abc import ABC, abstractmethod
import requests

class _GankBoardBaseObject(ABC):
    
    api_key = None

    url = "http://192.168.1.3/api"

    def request(self, method, endpoint, **kwargs):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        try:
            response = requests.request(method, f"{self.url}/{endpoint}", headers=headers, **kwargs)
            response.raise_for_status()
            return response.status_code, response.json()
        except requests.exceptions.RequestException as e:
            return None, {'error': str(e)}


    @abstractmethod
    def delete(self, resource_id):
        """
        Supprime une ressource par son ID.
        """
        pass

    @abstractmethod
    def modify(self, **kwargs):
        """
        Modifie une ressource existante par son ID.
        """
        pass
    
    @abstractmethod
    def create(self, **kwargs):
        pass
