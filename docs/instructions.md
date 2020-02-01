# How to start the proyect

### Docker

Run inside the proyect folder

    docker-compose up

### Venv

Requires python 3

Create venv (proyect folder)

    python3 -m venv src/venv

Activate venv

    . src/venv/bin/activate

Install dependencies

    pip install -r src/requirements.txt -r src/requirements.dev.txt

To deactivate venv

    deactivate


# Database

To initialize migrations

    flask db init

To detect migrations 

    flask db migrate

To apply migrations

    flask db upgrade

More info about [Flask-Migrate ](https://flask-migrate.readthedocs.io/en/latest/)

# Lint

To run flake8

    docker exec -it ze_challenge_backend_python_1 flake8 app