# How to start the proyect

Run inside the proyect folder

    docker-compose up


# Database

To initialize migrations

    flask db init

To detect migrations 

    flask db migrate

To apply migrations

    flask db upgrade

More info about [Flask-Migrate ](https://flask-migrate.readthedocs.io/en/latest/)