# Loft Test - Ground Software

## Hello World!

I haven't used Django in many years. My current employer built their own async ground software on top of the aiohttp library. Most recently, I use a MVC framework in Julia called Genie. I like it a lot. For this quiz, I used a [Hello World example](https://djangoforbeginners.com/hello-world/) to get all the syntax and conventions right for Django.

## Run with docker

```
docker build -t loftorbitalapp:latest .
docker build -t loftorbitalconsumer:latest .
```

TODO: some docker-compose thing for the temperature source container
and networking to share a localhost

The local SQLite database in the container should be filling up quickly!
Hurry up, make some queries.

## Make queries

The query interface is available and responds to the two queries in the instructions.

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
python -m pip install -r requirements.txt
pytest
```

## Swap out database and long term project discussion

Django abstracts a bunch of databases. To move to PostgreSQL in place would only require changing the adapter and running migrations on the new DB. But...this exercise is peculiar because it's leaning so heavily on the Django ORM.

I love ORMs for relational data but this is time series data. A special purpose database like TimescaleDB, which can run within PostgreSQL would be better suited for scaling out to tens of thousands of measurements.

Another concern is queue scalability. Because this is an exercise, the easiest way to get an in-memory queue was to just lean on the websocket library. That gives us a small buffer in the event the app server is down but the data consumer service is running. A better way would be to introduce a message queue, I'm fond of ZeroMQ (but I've most recently deployed RabbitMQ) and rather than saving the messages to the program's memory, it would publish a message and zmq would subscribe to that source.

To further simplify things, the temperature readings would publish directly to the queue and the subscription microservice would pull off that queue.  The function that calls the GraphQL mutation would then subscribe to that queue topic and use the same write method to persist data. So yeah, pub/sub and topic based queues would be good for future improvements.
## Opinions

* [Hasura seems to be good](https://hasura.io/blog/turn-your-python-rest-api-to-graphql-using-hasura-actions/)
* [Can't figure out how to make the Django query return? Thanks Internet!](https://stackoverflow.com/questions/70920770/how-to-make-graphql-query-that-can-find-latest-or-min-or-max)
* From the time of this writing to today, the django-channels-graphql-ws library is broken! Yea. That made the subscription part go from the easiest part to the most confusing. +2 hours. Thanks coding quiz! A nice person from [three weeks ago](https://github.com/datadvance/DjangoChannelsGraphqlWs/issues/103) helped me out!
* [Django channels](https://realpython.com/getting-started-with-django-channels/) tutorial on how to use websockets. Still not sure how to subscribe to the feed and save points in the model.