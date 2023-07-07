import graphene
from graphene_django import DjangoObjectType

from tempquiz.models import Temperature

class TemperatureType(DjangoObjectType):
    class Meta:
        model = Temperature
        fields = ("id", "timestamp", "value")

class Query(graphene.ObjectType):
    current_temperature = graphene.List(TemperatureType)
    temperature_statistics = graphene.List(TemperatureType)

    def resolve_current_temperature(root, info, **kwargs):
        return Temperature.objects.all()

    def resolve_temperature_statistics(root, info, **kwargs):
        return Temperature.objects.max(value=value)

schema = graphene.Schema(query=Query)