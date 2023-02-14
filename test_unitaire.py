# Fonctiond e test unitaire servant à vérifier le bon déploiement de l'API

# Import des librairies
from app import get_data
from app import client_data(
import json

# Fonction de test
def test_client_data():
    requete_json = app.client_data("222231")
    # json.loads("https://api-flask-ocr-projet-7.herokuapp.com/data/client/222231")
    print(requete_json)
    print(requete_json["BURO_CREDIT_ACTIVE_cat_Active_MEAN"])
    expected = [1.0, -0.061780218046809325]
    assert expected == requete_json["BURO_CREDIT_ACTIVE_cat_Active_MEAN"]