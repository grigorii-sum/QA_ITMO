FROM python:3

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /site
COPY . /site
WORKDIR /site

RUN pip install --upgrate pip
RUN pip instal requirements.txt

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "127.0.0.0:8000"]