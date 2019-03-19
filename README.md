# LOG8371
tp pour le cours de qualité

## pour rouler les containers docker :

cd TP2/
### Cette commande va build l'image docker de weka rest avec une instance jprofiler dedans.
docker build -t jguweka_log8371:v1 .

### Cette commande va lancer les container docker et rendre weka rest disponible sur le port 8081. (http://localhost:8081)
docker-compose up

## Pour mettre en place Jprofiler

### Ouvrir un nouveau terminal

### Cette commande va servire a rentrer dans le container docker de weka rest pour y activer jprofiler (tuto complet : http://geekspearls.blogspot.com/2016/08/configure-jprofiler-92-to-profiling.html)

docker exec -it wekarest bash 

### Une fois dans le container rouler les commandes suivantes :

* cd /usr/local/jprofiler9/
* bin/jpenable

### Ensuite un choix entre 1 ou 2 vous sera proposez. Entrer 1
### Ensuite on vous demandera sur quel port jprofiler devra etre exposer. Entrer 8849

## Installer la version 9.2 de jprofiler
* Aller a cette addresse la : https://www.ej-technologies.com/download/jprofiler/version_92
* Telecharger Jprofiler 9.2

### Aller sur le GUI de jprofiler et connecter vous a un remote process.
* Entrer le ip de votre docker (peut etre trouver a l'aide de __docker info__)
* Entrer le port 8849
