import graphene
from graphene_django import DjangoObjectType

from tempquiz.models import Temperature

class TemperatureType(DjangoObjectType):
    class Meta:
        model = Temperature
        fields = ("time", "temperature")

class Query(graphene.ObjectType):
    current_temperature = graphene.List(TemperatureType)
    min_max_temperature = graphene.List(TemperatureType)

    def resolve_current_temperature(root, info):
        return Temperature.objects.select_related("temperature").last()
    
    def resolve_min_max_temperature(root, info, time):
        try:
            before = Temperature.objects.get(time="2020-12-07T12:00:00+00:00")
            after = Temperature.objects.get(time="2020-12-06T12:00:00+00:00")
            return []
        except Temperature.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)