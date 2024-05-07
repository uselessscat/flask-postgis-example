# How to start the project

## Docker

Run inside the project folder

```sh
docker compose up
```

## Venv

Requires python 3

Create venv (project folder)

```sh
python3 -m venv src/.venv
```

Activate venv

```sh
. ./src/.venv/bin/activate
. ./src/.venv/Scripts/activate
```

Install dependencies

```sh
pip install -r src/requirements.txt -r src/requirements.dev.txt
```

To deactivate venv

```sh
deactivate
```

## Database

To initialize migrations

```sh
docker exec -it flask-postgis-example_python_1 flask db init
```

To detect migrations

```sh
docker exec -it flask-postgis-example_python_1 flask db migrate
```

To apply migrations

```sh
docker exec -it flask-postgis-example_python_1 flask db upgrade
```

More info about [Flask-Migrate ](https://flask-migrate.readthedocs.io/en/latest/)

## Testing

Create a db with something like

```sql
CREATE DATABASE postgis_example_testing;
CREATE EXTENSION postgis;
```

To run tests

```sh
docker exec -it flask-postgis-example_python_1 pytest
```

Test coverage (using html report)

```sh
docker exec -it flask-postgis-example_python_1 bash -c 'coverage run -m pytest && coverage html'
```

## Lint

To run flake8

```sh
docker exec -it flask-postgis-example_python_1 flake8
```

To run type checking

```sh
docker exec -it flask-postgis-example_python_1 mypy
```
