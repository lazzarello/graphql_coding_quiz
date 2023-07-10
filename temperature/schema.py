import channels_graphql_ws
import graphene
from graphene_django import DjangoObjectType
from django.db.models import Max, Min

from tempquiz.models import Temperature

class TemperatureSub(channels_graphql_ws.Subscription):
    """Get Temperatures"""
    notification_queue_limit = 1000

    event = graphene.String()

    class Arguments:
        timestamp = graphene.String()
        value = graphene.String()

    @staticmethod
    def publish(payload, info, timestamp, value):
        """Send a subscribe query to the temp endpoint"""
        return TemperatureSub(event="wtf")

    @staticmethod
    def subscribe(root, info, timestamp, value):
        """Called when some mysterious user subscribes..."""
        pass

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
        
        if before and after:
            range_type.max = Temperature.objects.filter(
                timestamp__gte=after,
                timestamp__lte=before).aggregate(Max('value'))['value__max']
            range_type.min = Temperature.objects.filter(
                timestamp__gte=after,
                timestamp__lte=before).aggregate(Min('value'))['value__min']
            return range_type
        elif before:
            range_type.max = Temperature.objects.filter(
                timestamp__lte=before).aggregate(Max('value'))['value__max']
            range_type.min = Temperature.objects.filter(
                timestamp__lte=before).aggregate(Min('value'))['value__min']
            return range_type
        elif after:
            range_type.max = Temperature.objects.filter(
                timestamp__gte=after).aggregate(Max('value'))['value__max']
            range_type.min = Temperature.objects.filter(
                timestamp__gte=after,).aggregate(Min('value'))['value__min']
            return range_type
        else:
            range_type.max = Temperature.objects.all().aggregate(
                Max('value'))['value__max']
            range_type.min = Temperature.objects.all().aggregate(
                Min('value'))['value__min']
            return range_type

class CreateTemperature(graphene.Mutation):
    class Arguments:
        value = graphene.Float()
    ok = graphene.Boolean()
    temperature = graphene.Field(TemperatureType)

    def mutate(root, info, value):
        temperature = Temperature(value=value)
        temperature.save()
        ok = True
        return CreateTemperature(temperature=temperature, ok=ok)

class Mutation(graphene.ObjectType):
    create_temperature = CreateTemperature.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)