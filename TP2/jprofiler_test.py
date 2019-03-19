import requests
import json

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

for url_ in list_GET_REST_request:
    response = requests.get(
    url= url_,
    headers=headers
    )
    data = response.json()
    print(json.dumps(data, indent=4))