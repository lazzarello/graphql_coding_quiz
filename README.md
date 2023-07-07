# Loft Test - Ground Software

## Hello World!

I haven't used Django in many years. My current employer built their own async ground software on top of the aiohttp library. Most recently, I use a MVC framework in Julia called Genie. I like it a lot. For this quiz, I used a [Hello World example](https://djangoforbeginners.com/hello-world/) to get all the syntax and conventions right for Django.

## Run with docker

`docker run -p 8000:8000 -it loftorbitaltest:latest`

TODO: some docker-compose thing for the temperature source container
and networking to share a localhost

## Look at website

http://127.0.0.1:8000/

## Wanna make changes?

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

https://hasura.io/blog/turn-your-python-rest-api-to-graphql-using-hasura-actions/