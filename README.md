# QA_ITMO

## IMPORTANT

pip3 install django

virtualenv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver

## NOT IMPORTANT

coverage run --source='./main' manage.py test .

coverage report

