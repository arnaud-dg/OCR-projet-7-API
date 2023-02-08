# -----------------------------------------------------------------------------------------
# -----------------------     Création de l'API avec FLASK   ------------------------------
# -----------------------------------------------------------------------------------------

# API servant à charger les données des clients, à prédire le score à travers le modèle et à produire les SHAP values

# Import des librairies requises
# Génériques
import os
import numpy as np
import pandas as pd
# API Flask + modele
import flask
from flask import jsonify
from flask import request
import pickle
# SHAP Values
import shap

# Initialisation de l'API
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Chemin du repertoire où sont stockés les fichiers
path = os.path.dirname(os.path.realpath(__file__))

# ------------------------------       HOME       --------------------------------------
# Page accueil
@app.route('/', methods=['GET'])
def home():
    return """
<h1>Projet #7 - Implémentez un modèle de scoring (A.Duigou) - 02.2023</h1>
<p>Cet API va assurer plusieurs rôles:
charger les données des clients (pour un groupe de client ou un client seul) / 
charger le modèle de classification et prédire le score d'un client donné / 
produire les shap values pour l'interprétabilité de la prédiction
 </p>
"""

# Chargement du modèle optimisé enregistré sous forme binaire/pickle
modele=pickle.load(open(path + "/model_2.pkl","rb"))
# Chargement des données test (chargement d'un échantillon uniquement)
X=pd.read_csv(path + "/data_sample.csv")

# -------------------       Affichage ensemble dataset       ---------------------------
# Création d'une route pour récupérer les données clients
@app.route("/data", methods=["GET"])
def get_data():
    df = X.to_dict("list")
    return jsonify(df)

# ------------------       Affichage client ID spécifique       -------------------------
# Création d'une route pour récupérer les données clients et effectuer les prédictions
@app.route("/data/client/<client_id>", methods=["GET"])
def client_data(client_id):
    # Filtre des données sur la base de l'ID client
    df_short=X[X["SK_ID_CURR"] == int(client_id)]
    features=np.asarray(df_short.iloc[0,1:21]) # Extraction des features caractéristiques

    # Calcul de la prédiction et de la probabilité pour le client - Ajout au dataframe filtré
    df_short["prediction"]=modele.predict([features]).tolist()[0] # Prédiction de la classe
    df_short['proba_1']=modele.predict_proba([features])[:,1].tolist()[0] # Prédiction de la probabilité

    # Calcul de la feature importance
    explainer=shap.KernelExplainer(model.predict_proba, X.iloc[:,1:21]) 
    shap_values=explainer.shap_values(features, l1_reg="aic")

    # Ajout des SHAP values dans le Dataframe
    df_short["expected"]=explainer.expected_value[1]
    new_line=[99999] + list(shap_values[1]) + [0,0,explainer.expected_value[1]] # Création d'un nouveau vecteur contenant les SHAP values
    df_short.loc[1]=new_line # Concaténation

    # Creation d'un dictionnaire 
    result=df_short.to_dict("list")

    # Retourne la prédiction sous forme d'un fichier json
    return jsonify(result)

# A retirer en ligne :
if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0')