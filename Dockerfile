FROM python:3.11.3

RUN mkdir /code
COPY . /code
WORKDIR /code
RUN python -m pip install -r requirements.txt
RUN python manage.py migrate
CMD ["gunicorn", "--bind=0.0.0.0", "temperature.wsgi"]