# Fonction de test unitaire servant à vérifier le bon déploiement de l'API

# Import des librairies
import pytest
# import flask
# from flask import jsonify
# from flask import request
# # from app import app as flask_app
# # from app import get_data
# # from app import client_data
# import json
# import numpy as np
# import pandas as pd

# Fonction de test
# @pytest.fixture
# def app():
#     yield flask_app

# @pytest.fixture
# def client(app):
#     return app.test_client()

# def test_get_data(app, client):
#     res = client.get('/data')
#     assert res.status_code == 200

from main import add_numbers
from main import home

def test_main():
    assert add_numbers(2, 3) == 5

def test_home():
    """
    Appel de la fonction gome pour vérifier les informations qui se chargent
    """
    # URL = "https://api-flask-ocr-projet-7.herokuapp.com/"
    response = main.get('/')
    print(response)
    print(response["BURO_CREDIT_ACTIVE_cat_Active_MEAN"])
    expected = [1.0, -0.061780218046809325]
    assert "Projet #7" in response
    assert expected == response["BURO_CREDIT_ACTIVE_cat_Active_MEAN"]
    assert response.status_code == 200