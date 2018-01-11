
# Volcano plot project

L’objectif de ce projet est d’implémenter un outil de visualisation pour l’analyse de données en protéomique
quantitative. Cet outil est intégré dans serveur virtuel  permettant aux utilisateur de  réaliser leurs
analyses en ligne.

## Dépendances

le fichier requirement.txt comporte tous les dépendances a installer

### installation d'un environnent virtuel et pip

__mise à jour de pip,  niveau utilisateur__  
python -m pip install pip --upgrade --user

__installation de l'environnement virtuel__  
pip install virtualenv

__activatetion de l'environnement virtuel__  
virtualenv -p python3 volcano-env
source volcano-env/bin/activate

__commande pour désativer l'environnement virtuel__  
deactivate

## installation des dépendances

pip install -r requirements.txt

__l’exécution du server se fait sous Linux__  

python routes.py
