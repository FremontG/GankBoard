# __init__.py

from Project import Project
from Report import Report
from Task import Task
from .abstract import _GankBoardBaseObject

# Définir les objets qui seront disponibles directement à partir de l'import du module "gankboard"
__all__ = ["Project", "Task","Report"]

# Définir la clé API globale initialement vide
api_key = None

# Associer la variable api_key à la clé API de _GankBoardBaseObject
def _set_api_key(key):
    global api_key
    api_key = key
    _GankBoardBaseObject.api_key = key

# Pour permettre l'attribution via gankboard.api_key = "nouvelle_clé"
class GankBoardModule:
    @property
    def api_key(self):
        return api_key

    @api_key.setter
    def api_key(self, key):
        _set_api_key(key)

# Créer une instance de GankBoardModule pour permettre l'accès via gankboard.api_key
gankboard = GankBoardModule()