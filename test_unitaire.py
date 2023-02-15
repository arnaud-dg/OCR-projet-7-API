# ------------------------------------------------------------------------
# Fonction de test unitaire servant à vérifier le bon déploiement de l'API
# ------------------------------------------------------------------------

# Import des librairies
import pytest
from main import add_numbers

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
    assert add_numbers(5, 1) == 6

