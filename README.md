# Bookshop with Flask-RESTful API
[![Build Status](https://travis-ci.com/yar-kik/DevelopsToday-test-project.svg?branch=master)](https://travis-ci.com/yar-kik/DevelopsToday-test-project)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3810/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Introduction
This is a simple news board API.
It have a list of news with functionality to upvote and comment on them. User also can register and login. Similar platform to [HackerNews](https://news.ycombinator.com/).
Deployed project is located at the [link](https://develops-today-test-project.herokuapp.com)

## Postman documentation 
* [Authentication](https://documenter.getpostman.com/view/14489034/TzeTLAXi)
* [News post management](https://documenter.getpostman.com/view/14489034/TzeTLAXm)
* [Post comments management](https://documenter.getpostman.com/view/14489034/TzeTLAXk)


## Technologies
Project uses such technologies:
* Django and DRF with JWT-token for auth
* PostgreSQL
* Docker for containerizing

## Requirements
You should have already installed Docker and Git. 

## Usage
Get local copy of project with: 
```
git clone https://github.com/yar-kik/DevelopsToday-test-project.git
``` 

To build a production ready environment and start API server run:: 
```
docker-compose up -d
``` 
This may take a few minutes. Finally, your api will work on `http://localhost:8000/`.


