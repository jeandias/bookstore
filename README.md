# Bookstore
### Description
A simple book store REST API
## Installation
### Clone project
Clone project using Git over SSH.
```sh
$ git clone git@github.com:jeandias/bookstore.git
$ cd bookstore
```
### Install dependencies for project
```sh
$ docker build .
$ docker-compose build
$ docker-compose run web sh -c "python manage.py migrate"
$ docker-compose run web sh -c "python manage.py createsuperuser --email admin@example.com --username admin"
```
## Testing our API
```sh
$ docker-compose up -d
$ http://127.0.0.1:8000
```
