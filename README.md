# Yamdb
![example workflow](https://github.com/supermegacoolgirlwowyes/yamdb_final/actions/workflows/main.yml/badge.svg)

Yamdb service provides its users an access to the whole world of criticizing something that other people have created. Let's admit, we all love it.
## Getting Started

These instructions will get you a copy of the project up and running on your server for development, testing or production purposes.

### Prerequisites

Make sure your system is ready for running the project. Check if you have Git installed localy and Docker with Docker-compose installed on your server:
```
git version
```
```
docker --version
docker-compose --version
```
If not, follow this link for [git](https://github.com/git-guides/install-git) installation manual. Or these ones to install [docker](https://docs.docker.com/get-docker) and [docker-compose](https://docs.docker.com/compose/install/).

You may want to cusotmize the project at some point later. To be able to do so, fork from the original repository first.
[Original Repository on GitHub](https://github.com/Supermegacoolgirlwowyes/final_yamdb.git). While there, create a new workflow - you will need it later on.

Navigate to the working directory on your local machine and clone the project from the forked version. 

```
git clone https://github.com/<your_github_name>/final_yamdb.git
```

### Installing

Locally make a copy of the included **.env.template** and name it **.env**. 

```
cp .env.template .env
```
Declare your own environment variables in **.env** and save changes. Upload **.env**, **docker-compose.yaml** and **nginx/nginx.conf** to your server.

You are now set up to run the containers. Log in to your server and run the following command:


```
docker-compose up -d --build
```
This command will pull up the App, Postgres Database and Nginx server from Docker Hub and run the containers. The "-d" flag will make them run in a detached mode and will let you keep working in the same tab.

Once the containers are running:
(i) migrate the models to your newly created database, (ii) create superuser, (iii) load initial data from fixtures.json and (iv) collect static files into designated folder. 

```
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py loaddata fixtures.json
docker-compose exec web python manage.py collectstatic --no-input
```

Now your project is running at **your.server.ip.address**.

Django admin interface is available at **<ip_address>/admin**. Yamdb documentation is available at **<ip_address>/redoc**.

### Updating

This project is ready for Continuois Integration.

Copy code from **yamdb_workflow.yml** file to the earlier created **main.yml**. Set up environment variables using GitHub secrets (Settings > Secrets).

Whenever you need to apply your updates to the project, push them to the master branch. The workflow will automatically run the tests, create new Docker image, upload it to the DockerHub and Deploy your project. If the workflow is successful, you will receive a confirmation message on Telegram. Sweet :)


## Built With
* [Django](https://www.djangoproject.com) - Python web framework
* [Django REST](https://www.django-rest-framework.org) -  a toolkit for building Web APIs
* [PosetgreSQL](https://www.postgresql.org) - object-relational database system
* [Docker](https://www.docker.com) - containerization platform
* [Nginx](https://nginx.org/en/) - HTTP and reverse proxy server
* [Gunicorn](https://gunicorn.org) - Python WSGI HTTP Server

## Authors

* **Irina Egorova** - *Comments and Reviews, Dockerizing, Project Infrastructure* - [Supermegacoolgirlwowyes](https://github.com/Supermegacoolgirlwowyes)
* **Andrey Zhelezo** - *Users and Auth* - [Azhelezo](https://github.com/azhelezo)
* **Dmitriy Belokon** - *Titles, Categories and Genres* - [Mezander](https://github.com/Mezander)


## License

This product is not real. Nothing is real.

