# QA_ITMO

### important

virtualenv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver

### not important

coverage run --source='./main' manage.py test .

coverage report

