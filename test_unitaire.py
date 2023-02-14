# Fonctiond e test unitaire servant à vérifier le bon déploiement de l'API

# Import des librairies
pip install pytest
import pytest
from app import app as flask_app
import json

# Ajout du décorateur - fonction app()
@pytest.fixture
def app():
    yield flask_app

# Ajout du décorateur - fonction client()
@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))