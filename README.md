# Yamdb
![example workflow](https://github.com/supermegacoolgirlwowyes/yamdb_final/actions/workflows/main.yml/badge.svg)

Yamdb service provides its users an access to the whole world of criticizing something that other people have created. Let's admit, we all love it.
### Getting Started

These instructions will get you a copy of the project up and running on your server for development, testing or production purposes.

### Prerequisites

Make sure your system is ready for running the project. Check if you have Git installed locally and Docker with Docker-compose installed on your server:
```
git version
```
```
docker --version
docker-compose --version
```
If not, follow this link for [git](https://github.com/git-guides/install-git) installation manual. Or these ones to install [docker](https://docs.docker.com/get-docker) and [docker-compose](https://docs.docker.com/compose/install/).

You may want to customize the project at some point in the future. To be able to do so, fork from the [GitHub Original Repository](https://github.com/Supermegacoolgirlwowyes/final_yamdb.git) first. While there, create a new workflow - you will need it later on.

Navigate to the working directory on your local machine and clone the project from the forked version. 

```
git clone https://github.com/<your_github_name>/final_yamdb.git
```

### Deploying

Locally make a copy of the included **.env.template** and name it **.env**. 

```
cp .env.template .env
```
Declare your own environment variables in **.env** and save changes. Upload **.env**, **docker-compose.yaml** and **nginx/nginx.conf** to your server.

You are now set up to run the containers. Log in to your server and run the following command:


```
docker-compose up -d
```
This command will pull up the App, Postgres Database and Nginx server images from Docker Hub and run the containers. The '-d' flag will make them run in a detached mode and will let you keep working in the same tab.

**Docker-compose.yml** is set up to apply migrations and collect static files for you. You only need to create a superuser and load initial data if needed (you can go with included **fixtures.json** file or make your own).

```
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py loaddata fixtures.json
```

Now your project is running at **your.server.ip.address**.

Django admin interface is available at **<ip_address>/admin**. Yamdb documentation is available at **<ip_address>/redoc**.

### Updating

This project is ready for Continuous Integration.

Copy code from **yamdb_workflow.yml** file to the earlier created **main.yml**. Specify your project path as a target for your *docker-compose* and *nginx* files in *deploy*. Set up environment variables using GitHub secrets (Settings > Secrets).

Whenever you need to implement your updates to the project, push them to the master branch. The workflow will automatically run the tests, create new Docker image, upload it to the DockerHub and Deploy your project. If the workflow runs successfully, you will receive a confirmation message on Telegram. Sweet :)


## Built With
* [Django](https://www.djangoproject.com) - Python web framework
* [Django REST](https://www.django-rest-framework.org) -  a toolkit for building Web APIs
* [PosetgreSQL](https://www.postgresql.org) - object-relational database system
* [Docker](https://www.docker.com) - containerization platform
* [Nginx](https://nginx.org/en/) - HTTP and reverse proxy server
* [Gunicorn](https://gunicorn.org) - Python WSGI HTTP Server

## Authors

* **Irina Balerina** - *Comments and Reviews, Dockerizing, Project Infrastructure, Continuous Integration* - [Supermegacoolgirlwowyes](https://github.com/Supermegacoolgirlwowyes)
* **Andrey Zhelezo** - *Users and Auth* - [Azhelezo](https://github.com/azhelezo), [Supermegacoolgirlwowyes](https://github.com/Supermegacoolgirlwowyes)
* **Dmitriy Belokon** - *Titles, Categories and Genres* - [Mezander](https://github.com/Mezander)


## License

This product is not real. Nothing is real.
