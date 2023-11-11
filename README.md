<div align="center">

  <a href="">[![Pytest Testing Suite](https://github.com/drorganvidez/flask_base/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/drorganvidez/flask_base/actions/workflows/tests.yml)</a>
  <a href="">[![Commits Syntax Checker](https://github.com/drorganvidez/flask_base/actions/workflows/commits.yml/badge.svg?branch=main)](https://github.com/drorganvidez/flask_base/actions/workflows/commits.yml)</a>
  
</div>

# flask_boilerplate

Base project to work with the Python Flask framework in an easy way.

## Set `.env` file in root with:

Create an `.env` file in the root of the project with this information.

```
FLASK_APP_NAME=flask_base
MYSQL_HOSTNAME=db
MYSQL_DATABASE=flask_base_db
MYSQL_USER=flask_base_user
MYSQL_PASSWORD=flask_base_pass
MYSQL_ROOT_PASSWORD=flask_base_root_pass
```

## Deploy in develop

To deploy the software under development environment, run:

```
docker compose -f docker-compose.dev.yml up -d 
```

This will apply the migrations to the database and run the Flask application. Open `http://localhost` to play with your fantastic app!

### Migrations

However, if during development there are new changes in the model, run inside the `web` container:

```
flask db migrate
flask db upgrade
```

### Tests

To run unit test, please enter inside `web` container:

```
pytest app/tests/units.py
```

## Deploy in production (Docker Compose)

```
docker compose -f docker-compose.prod.yml up -d 
```

## SSL certificates

To generate a new certificate, run in deploy server: 

```
chmod +x ssl_setup.sh && ./ssl_setup.sh
```

To renew a certificate that is less than 60 days from expiry, execute in deploy server:

```
chmod +x ssl_renew.sh && ./ssl_renew.sh
```

## Update dependencies

To update all project dependencies automatically, run:

```
chmod +x update_dependencies.sh && ./update_dependencies.sh
```

Note: it is the responsibility of the developer to check that the update of the dependencies has not broken any functionality and each dependency maintains backwards compatibility. Use the script with care!

## Add new module

To add a new module or functionality to the project, an automatic script is provided:

```
python new_module.py
```

This will create a folder in `app` with the name of the module and a file and directory structure according to the project.

