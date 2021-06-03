# Django PDF Genarator API

Django sample rest api for creating pdf data.

```sh
$ docker-compose up --build
$ docker-compose run django /bin/sh

# in container
$ pipenv run python manage.py migrate

# exit container by pressing Ctrl + D

```

by requesting using POST method to `http://localhost:8080/api/pdf-export/`, you can get binary pdf data from this API.
