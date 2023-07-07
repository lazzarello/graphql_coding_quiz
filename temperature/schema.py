import graphene
from graphene_django import DjangoObjectType

from tempquiz.models import Temperature

class TemperatureType(DjangoObjectType):
    class Meta:
        model = Temperature
        fields = ("id", "time", "temperature")

class Query(graphene.ObjectType):
    temperatures = graphene.List(TemperatureType)

    def resolve_temperatures(root, info):
        return Temperature.objects.all()

schema = graphene.Schema(query=Query)