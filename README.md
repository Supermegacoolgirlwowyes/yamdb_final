# Yamdb
![example workflow](https://github.com/supermegacoolgirlwowyes/yamdb_final/actions/workflows/main.yml/badge.svg)

Yamdb service provides its users an access to the whole world of criticizing something that other people have created. Let's admit, we all love it.
## Getting Started

These instructions will get you a copy of the project up and running on your server for development, testing or production purposes.

### Prerequisites

Make sure your system is ready for running the project. Check if you have Git and Docker installed:
```
git version
docker --version
```
If not, follow this link for [git](https://github.com/git-guides/install-git) installation manual. Or this one to install [docker](https://docs.docker.com/get-docker).

Navigate to your working directory and clone the project from GitHub. 

```
git clone https://github.com/Supermegacoolgirlwowyes/final_yamdb.git
```

### Installing

Find included **.env.template** in the main project directory. Make a renamed copy.

```
cp .env.template .env
```

Declare your own environment variables in **.env** and save changes.

Run the containers with the following command.


```
docker-compose up -d --build
```
The "-d" flag will run the containers in a detached mode and will let you work in the same tab. And "--build" will build a new image from the Dockerfile before running the containers.

Once the containers are running:
(i) migrate the models to your newly created database, (ii) create superuser, (iii) load initial data from fixtures.json and (iv) collect static files into designated folder. 

```
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py loaddata fixtures.json
docker-compose exec web python manage.py collectstatic --no-input
```

Your project is running locally at [127.0.0.1](127.0.0.1).

Django admin interface at [127.0.0.1/admin](127.0.0.1/admin).

Yamdb documentation is available at [127.0.0.1/redoc](127.0.0.1/redoc).


## Built With
* [Django](https://www.djangoproject.com) - Python web framework
* [Django REST](https://www.django-rest-framework.org) -  a toolkit for building Web APIs
* [PosetgreSQL](https://www.postgresql.org) - object-relational database system
* [Docker](https://www.docker.com) - containerization platform
* [Nginx](https://nginx.org/en/) - HTTP and reverse proxy server
* [Gunicorn](https://gunicorn.org) - Python WSGI HTTP Server

## Authors

* **Andrey Zhelezo** - *Users and Auth* - [Azhelezo](https://github.com/azhelezo)
* **Dmitriy Belokon** - *Titles, Categories and Genres* - [Mezander](https://github.com/Mezander)
* **Irina Egorova** - *Comments and Reviews, Dockerizing, Project Infrastructure* - [Supermegacoolgirlwowyes](https://github.com/Supermegacoolgirlwowyes)


## License

This product is not real. Nothing is real.

