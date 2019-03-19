import requests
import json
from threading import Thread
from sys import argv as args

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

def rest_call():
   comp = 0
   # print("In thread : " + threadName)
   for url_ in list_GET_REST_request:
    comp += 1
    response = requests.get(
    url= url_,
    headers=headers
    )
    data = response.json()
    print("Requete #" + str(comp) + "\tGET " + url_ + "\t\t" + str(response.status_code))
    #print(json.dumps(data, indent=4))
   pass

def cas_reduit():
   # Charge réduite (sous 25% de CPU --> 5 requetes séquencielles) 
   rest_call()

def cas_moyen():
   # charge moyenne (entre 25% et 50% de CPU --> 12 requetes séquencielles)
   threads = []
   for x in range(0, 2):
      t1=Thread( target=rest_call)
      threads.append(t1)
      t1.start()

def cas_augmenter():
   # charge charge augmentée (entre 50% et 75% de CPU --> )
   threads = []
   for x in range(0,4):
      t1=Thread( target=rest_call)
      threads.append(t1)
      t1.start()
   pass


def cas_exceptionnelle():
   # charge augmentée exceptionnelle (entre 75% et 100% --> )
   threads = []
   for x in range(0,100):
      t1=Thread( target=rest_call)
      threads.append(t1)
      t1.start()
   pass

if args[1] == "--reduit" or args[1] == "1":
   print("Cas reduit")
   cas_reduit()
elif args[1] == "--moyen" or args[1] == "2":
   print("Cas moyen")
   cas_moyen()
elif args[1] == "--augmenter" or args[1] == "3":
   print("Cas augmenter")
   cas_augmenter()
elif args[1] == "--exceptionnelle" or args[1] == "4":
   print("Cas exceptionnelle")
   cas_exceptionnelle()
else:
   print("argument invalide")