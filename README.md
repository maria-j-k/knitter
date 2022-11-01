# knitter

Application intended to help you organize your knitting and crochet related stuff.

## Description

Application will consist of:

- base of yarns that you have or dream of

- base of the projects you want to do

- base of the favourites yarn shops

- base of the projects you've already done with description and photos

- calculator helping you estimate the amount of yarn needed to accomplish the project (applies to the shawls for example)

## Run the app

create postgres database with the name `knitter`

#### run in Docker containter

run `docker-compose build`

#### run on your machine

install poetry

run `poetry install`

export environemental variable `DJANGO_CONFIGURATION="LocalDevelopment"`

run `python manage.py runserver`
