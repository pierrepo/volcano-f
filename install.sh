#installation d'un environnent virtuel avec pipenv

# mise à jour de pip,  niveau utilisateur
python -m pip install pip --upgrade --user
#installation de pipenv
python -m pip install pipenv --user

mkdir projet_volcano
cd projet_volcano

pipenv --python  3.6.2
pipenv install requests
