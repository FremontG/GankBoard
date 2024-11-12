import logging

# Logger pour tracer les changements de clé API et d'URL
logger = logging.getLogger(__name__)

# Variables globales pour stocker la clé API et l'URL
_api_key = None
_url = "http://office.fridmund-development.fr:8001/api"  # URL de base par défaut

def set_api_key(key):
    global _api_key
    if not key:
        raise ValueError("La clé API ne peut pas être vide.")
    _api_key = key
    logger.info(f"Clé API définie : {_api_key}")

def get_api_key():
    if _api_key is None:
        raise ValueError("La clé API doit être définie avant d'effectuer une requête.")
    return _api_key

def set_url(url):
    global _url
    if not url:
        raise ValueError("L'URL ne peut pas être vide.")
    _url = url
    logger.info(f"URL définie : {_url}")

def get_url():
    return _url
