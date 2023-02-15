# ------------------------------------------------------------------------
# Fonction de test unitaire servant à vérifier le bon déploiement de l'API
# ------------------------------------------------------------------------

# Import des librairies
import pytest
from main import add_numbers
from main import app
# import flask
# from flask import jsonify
# from flask import request
# import json


# Fonction de test
# @pytest.fixture
# def app():
#     yield flask_app

# @pytest.fixture
# def client(app):
#     return app.test_client()

def test_main():
    assert sum_numbers([1, 2, 3]) == 6

def test_home():
    """
    Appel de la fonction gome pour vérifier les informations qui se chargent
    """
    # URL = "https://api-flask-ocr-projet-7.herokuapp.com/"
    response = app.test_client().get('/')
    assert response.status_code == 200