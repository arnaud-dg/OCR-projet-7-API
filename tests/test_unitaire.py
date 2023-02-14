# Fonction de test unitaire servant à vérifier le bon déploiement de l'API

# Import des librairies
import pytest
from app import app
from app import get_data
from app import client_data
import json
import numpy as np
import pandas as pd

# Fonction de test
def test_get_data():
    """
    Appel de la fonction client_data (numer "222231") ET
    Vérification du contenu du fichier JSON
    """
    response = app.test_client().get('/')
    # json.loads("https://api-flask-ocr-projet-7.herokuapp.com/data/client/222231")
    print(response)
    print(response["BURO_CREDIT_ACTIVE_cat_Active_MEAN"])
    expected = [1.0, -0.061780218046809325]
    assert expected == response["BURO_CREDIT_ACTIVE_cat_Active_MEAN"]
    assert response.status_code == 200