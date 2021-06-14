# Bookshop with Flask-RESTful API
[![Build Status](https://travis-ci.com/yar-kik/DevelopsToday-test-project.svg?branch=master)](https://travis-ci.com/yar-kik/DevelopsToday-test-project)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Technologies
Project uses such technologies:
* Django and DRF with JWT-token for auth
* PostgreSQL
* Redis
* Docker for containerizing

## Requirements
You should have already installed Docker and Git. 

## Usage
Get local copy of project with: 
```
git clone https://github.com/yar-kik/DevelopsToday-test-project.git
``` 

To build a local development environment and start API server run:  
```
docker-compose -f docker-compose-dev.yml up -d 
``` 
Or you can build a production ready environment: 
```
docker-compose -f docker-compose.yml up -d
``` 
This may take a few minutes. Finally, your api will work on `http://localhost:8000/` 
if you start development configuration or on `http://localhost/` if you start production 
configs.
