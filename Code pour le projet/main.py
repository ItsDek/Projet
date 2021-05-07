#ici j'importe le package "json" et "requests" qui sont essentiels pour mon code.

import json
import requests

#Ici, j'ouvre les fichiers "tempsDattente", "numeroTransport" et "terminus", j'afficherai dedans les resultats de-
#mes requêtes.
tempsdattente9 = open('tempsDattente.h', 'w')
numerotransport9 = open('numerotransport.h', 'w')
terminus9 = open('terminus.h', 'w')
#ici ce passe la demande des données sur les serveurs de la STIB, c'est en gros la commande CURl mais en python.
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer IL FAUT METTRE SON TOKEN ICI',
}

response = requests.get('https://opendata-api.stib-mivb.be/OperationMonitoring/4.0/PassingTimeByPoint/5013B',headers=headers)


#convertis la réponse en .json
jsonResponse = response.json()

#ici j'affiche tout la réponse en json
print("Affichage de la réponse en de l'api:")
print(jsonResponse)

#ici, j'ai du faire un tour de passe passe car j'arrivais pas à parser directement la réponse,
#j'avais eu plusieurs erreur différentes jusqu'a trouver le bon moyen de le regler: https://stackoverflow.com/questions/42354001/python-json-object-must-be-str-bytes-or-bytearray-not-dict
parsed_json = json.dumps(jsonResponse)
wsh = json.loads(parsed_json)
#ici je "parse" la réponse, j'ai mis une image(arborescence.png) qui répresente l'arborescence de comment je reçois les données
#DU PROCHAIN BUS UNIQUEMENT (pas celui d'après donc)
print("testtest: ", wsh["points"][0]["passingTimes"])
print("jetest: ", wsh["points"][0]["passingTimes"][0]["destination"])
#ici, je met le terminus, l'heure d'arrivée et le numéro de la line dans des fichiers respectifs, que je vais utiliser avec
#mon code principale !
print("Terminus=: ", wsh["points"][0]["passingTimes"][0]["destination"]["fr"], file = terminus9)
print("Temps d'attente=:", wsh["points"][0]["passingTimes"][0]["expectedArrivalTime"], file = tempsdattente9)
print("Numéro=: ",wsh["points"][0]["passingTimes"][0]["lineId"], file = numerotransport9)



