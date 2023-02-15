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
from main import app

def test_main():
    assert sum_numbers([1, 2, 3]) == 6

def test_home():
    """
    Appel de la fonction gome pour vérifier les informations qui se chargent
    """
    # URL = "https://api-flask-ocr-projet-7.herokuapp.com/"
    response = app.testt_client().get('/')
    expected = "<h1>"
    assert expected in response