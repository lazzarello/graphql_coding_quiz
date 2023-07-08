import graphene
from graphene_django import DjangoObjectType
from django.db.models import Max, Min

from tempquiz.models import Temperature

class TemperatureType(DjangoObjectType):
    class Meta:
        model = Temperature
        fields = ("id", "timestamp", "value")

class AggregateType(graphene.ObjectType):
    min = graphene.String()
    max = graphene.String()

class Query(graphene.ObjectType):
    current_temperature = graphene.Field(TemperatureType)
    temperature_statistics = graphene.Field(
        AggregateType, before=graphene.String(), after=graphene.String()
    )

    def resolve_current_temperature(root, info):
        return Temperature.objects.last()

    def resolve_temperature_statistics(self, info, before=None, after=None):
        range_type = AggregateType()
        range_type.max = Temperature.objects.all().aggregate(Max('value'))['value__max']
        range_type.min = Temperature.objects.all().aggregate(Min('value'))['value__min']
        return range_type

schema = graphene.Schema(query=Query)