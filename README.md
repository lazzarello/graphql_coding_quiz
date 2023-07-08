# Loft Test - Ground Software

## Hello World!

I haven't used Django in many years. My current employer built their own async ground software on top of the aiohttp library. Most recently, I use a MVC framework in Julia called Genie. I like it a lot. For this quiz, I used a [Hello World example](https://djangoforbeginners.com/hello-world/) to get all the syntax and conventions right for Django.

## Run with docker

```
docker build -t loftorbitaltest:latest .
docker run -p 8000:8000 -it loftorbitaltest:latest
```

TODO: some docker-compose thing for the temperature source container
and networking to share a localhost

## Look at website

http://127.0.0.1:8000/graphql

## Wanna make a change?

```
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py runserver
```

## Run tests

```
source .venv/bin/activate
python manage.py test
```

## Swap out database

## Opinions

* [Hasura seems to be good](https://hasura.io/blog/turn-your-python-rest-api-to-graphql-using-hasura-actions/)
* [Can't figure out how to make the Django query return? Thanks Internet!](https://stackoverflow.com/questions/70920770/how-to-make-graphql-query-that-can-find-latest-or-min-or-max)
* From the time of this writing to today, the django-channels-graphql-ws library is broken! Yea. That made the subscription part go from the easiest part to the most confusing. +2 hours. Thanks coding quiz! A nice person from [three weeks ago](https://github.com/datadvance/DjangoChannelsGraphqlWs/issues/103) helped me out!