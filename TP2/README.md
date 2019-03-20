# Analyse avec JProfiler
Téléchargez la version 9.2 de Jprofiler : http://download-keycdn.ej-technologies.com/jprofiler/jprofiler_linux_9_2.tar.gz

Ouvrez un **terminal**

Aller sur l'emplacement où le Jprofiler 9.2 a été installé.

rouler la commande suivante : bin/jprofiler

# Loader notre snapshoot

Une fois jprofiler ouvert : 
* selectionner "__profile a demo session or a saved session__" > "__Open Snapshots__" > "__open a single snapshoot__"
* Naviger dans notre repertoire de remise et aller ouvrir la fichier __Q3_profile.jps__
* Nos enregistrements s'affichent à l'écran.
  
# Analyse des résultats
* Le premier pic correspond au cas reduit
* Le 2e pic correspond au cas moyen
* Le 3e pic correspond au cas augmenter
* Le 4e pic correspond au cas exceptionnelle