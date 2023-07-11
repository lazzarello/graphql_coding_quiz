# Temperature Test 

## Hello World!

I haven't used Django in many years. I'm more familliar with a codebase from an employer built with the aiohttp library. Most recently, I use a MVC framework in Julia called Genie. I like it a lot. For this quiz, I used a [Hello World example](https://djangoforbeginners.com/hello-world/) to get all the syntax and conventions right for Django.

I have pyenv set up on my personal dev machine. I used 3.11.3 locally, which is the same version in the Dockerfile.

## Run with docker

```
docker build -t app:latest -f Dockerfile .
docker build -t broker:latest -f Dockerfile_broker .
docker-compose up
```

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

The Django admin interface is enabled after you set the superuser password via manage.py. There's also a mutation in the GraphQL schema that adds points.

The broker is just a normal python program `python websocket_sub.py`

## Run tests

```
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest
```

## Swap out database and long term project discussion

Django abstracts a bunch of databases. To move to PostgreSQL in place would only require changing the adapter and running migrations on the new DB. But...this exercise is peculiar because it's leaning so heavily on the Django ORM.

I love ORMs for relational data but this is time series data. A special purpose database like TimescaleDB, which can run within PostgreSQL would be better suited for scaling out to tens of thousands of measurements.

Another concern is queue scalability. Because this is an exercise, the easiest way to get an in-memory queue was to lean on the websocket library. That gives us a small buffer in the event the app server is down but the data consumer service is running. A better way would be to introduce a message queue, I'm fond of ZeroMQ (but I've most recently deployed RabbitMQ) and rather than saving the messages to the program's memory, it would publish a message and zmq would subscribe to that source.

To further simplify things, Pub/Sub and topic based queues would be good for future improvements. The temperature readings would publish directly to the queue and the subscription microservice would pull off that queue.  The function that calls the GraphQL mutation would then subscribe to that queue topic and use the same write method to persist data. 

## Production deployment

I set up the Django web app to use guinicorn and the broker uses asyncio which should be good for a while until the message queue interface is built.
Putting the broker into an app server container might also make sense to handle more concurrency.

I'd like to scale this out with Kubernetes, where I would have a number of deployments using the internal DNS to communicate as services rather than the docker-compose host network like in this example. The services would include

* Django webapp backed by a relational database
* A message queue
* The measurement reading
* The measurement consumer
* A front end load balancer for all the javascript I didn't demonstrate for this quiz
* An Ingress for the web application

Most of this would be triggered via CI pipelines (I'm most familliar with Gitlab but I use Github for public projects) so things like images, manifests and rolling updates could be built via CI jobs. Much of my niche expertise in scaling out ground software in aerospace leans on Kubernetes and AWS external service integrations. I have Terraform to manage all that.

I just noticed the development docker images are pretty big. I'd optimize them for size for production deployments. I think I could at least half the size by using the Alpine Linux python image.

## Opinions on This Journey

* [Hasura seems to be good for a generic REST to GraphQL system](https://hasura.io/blog/turn-your-python-rest-api-to-graphql-using-hasura-actions/)
* [Can't figure out how to make the min/max thing work? Thanks Internet!](https://stackoverflow.com/questions/70920770/how-to-make-graphql-query-that-can-find-latest-or-min-or-max)
* From the time of this writing to today, the django-channels-graphql-ws library is broken! Yea. That made the subscription part go from the easiest part to the most confusing. +2 hours. A nice person from [three weeks ago](https://github.com/datadvance/DjangoChannelsGraphqlWs/issues/103) helped me out!
* [Django channels](https://realpython.com/getting-started-with-django-channels/) tutorial on how to use websockets. Still not sure how to subscribe to the feed and save points in the model.