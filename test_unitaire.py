# Fonctiond e test unitaire servant à vérifier le bon déploiement de l'API

# Import des librairies
from app import get_data
import json

# Fonction de test
def test_get_data():
    expected = {'hello': 'world'}
    assert expected == json.loads(get_data())