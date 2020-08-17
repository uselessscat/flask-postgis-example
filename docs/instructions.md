# How to start the proyect

### Docker

Run inside the proyect folder

    docker-compose up

### Venv

Requires python 3

Create venv (proyect folder)

    python3 -m venv src/venv

Activate venv

    . ./src/venv/bin/activate
    . ./src/venv/Scripts/activate

Install dependencies

    pip install -r src/requirements.txt -r src/requirements.dev.txt

To deactivate venv

    deactivate


# Database

To initialize migrations

    docker exec -it flask-postgis-example_python_1 flask db init

To detect migrations 

    docker exec -it flask-postgis-example_python_1 flask db migrate

To apply migrations

    docker exec -it flask-postgis-example_python_1 flask db upgrade

More info about [Flask-Migrate ](https://flask-migrate.readthedocs.io/en/latest/)

# Testing

Create a db with something like

    CREATE DATABASE postgis_example_testing;
    CREATE EXTENSION postgis;

To run tests

    docker exec -it flask-postgis-example_python_1 pytest

Test coverage (using html report)

    docker exec -it flask-postgis-example_python_1 bash -c 'coverage run -m pytest && coverage html'

# Lint

To run flake8

    docker exec -it flask-postgis-example_python_1 flake8

To run type checking

    docker exec -it flask-postgis-example_python_1 mypy
