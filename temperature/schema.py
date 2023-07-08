import graphene
from graphene_django import DjangoObjectType
from django.db.models import Max, Min

from tempquiz.models import Temperature

class TemperatureType(DjangoObjectType):
    class Meta:
        model = Temperature
        fields = ("id", "timestamp", "value", "max", "min")

class Query(graphene.ObjectType):
    current_temperature = graphene.Field(TemperatureType)
    temperature_statistics = graphene.Field(TemperatureType)

    def resolve_current_temperature(root, info):
        return Temperature.objects.last()

    def resolve_temperature_statistics(root, info):
        max = Temperature.objects.all().aggregate(Max('value'))['value__max']
        min = Temperature.objects.all().aggregate(Min('value'))['value__min']
        # probably need to filter on value__max and value__min
        # using the graphene python library and django-filter
        return [max, min]

schema = graphene.Schema(query=Query)