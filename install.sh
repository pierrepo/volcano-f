#installation d'un environnent virtuel avec pipenv


##AVEC PIPENV
# mise à jour de pip,  niveau utilisateur
python -m pip install pip --upgrade --user

#installation de pipenv
python -m pip install pipenv --user

#creation du ficher de test
mkdir projet_volcano_virt
cd projet_volcano_virt

#installation de l'environnement virtuel
pipenv --python  3.6.2

#installation des libraires
pipenv install requests
pipenv install flask
pipenv install pandas
pipenv install numpy

#creation du fichier de dépendances
pipenv lock -r > requirements.txt

#installation du ficier de dépendances
pipenv install -r requirements/txt

# VIRTUAL ENV ET PIP

pip install virtualenv

virtualenv -p python3 volcano-env
source volcano-env/bin/activate

pip freeze > requirements.txt
pip install -r requirements.txt

deactivate
