import requests
import json
import thread
import time

"""
Mise en place de l'url de base
"""
ip_url = "http://localhost"
port_url = "8081"
open_api = "/openapi"
base = ip_url + ":" + port_url + open_api

"""
Mise en place de toutes les url avec GET comme type de requet REST.
"""
algorithme_rest_url         = base + "/algorithm"
algorithme_generic_rest_url = base + "/algorithm/generic"
api_rest_url                = base + "/api/api.json"
data_set_rest_url           = base + "/dataset"
model_rest_url              = base + "/model"
task_rest_url               = base + "/task"

"""
Ajout de toutes les request GET REST dans une tableau
"""
list_GET_REST_request = []
list_GET_REST_request.append(algorithme_rest_url)
list_GET_REST_request.append(algorithme_generic_rest_url)
list_GET_REST_request.append(api_rest_url)
list_GET_REST_request.append(data_set_rest_url)
list_GET_REST_request.append(model_rest_url)
list_GET_REST_request.append(task_rest_url)


"""
Header pour les requests REST
"""
headers = {
   "Accept": "application/json"
}
comp = 0


# charge moyenne (12 requetes séquencielles)
def rest_call():
   for url_ in list_GET_REST_request:
    comp += 1
    response = requests.get(
    url= url_,
    headers=headers
    )
    data = response.json()
    print(comp)
    #print(json.dumps(data, indent=4))
   pass


# Charge réduite (6 requetes séquencielles)
rest_call()

# charge moyenne (12 requetes séquencielles)
for x in range(0, 2):
   rest_call()

# charge charge augmentée ()
# charge augmentée exceptionnelle ()