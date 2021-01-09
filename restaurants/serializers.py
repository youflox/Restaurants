from rest_framework import serializers

from .models import (
    RestaurantModel,
    RatingModel,
    TimeSlotsModel,
    TablesModel,
)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = RatingModel
        fields  = '__all__'

class RestaurentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantModel
        fields = ('id','name','image','category','price','ratings')
        read_only_fields = ['ratings',]

class TimeSlotsSeializer(serializers.ModelSerializer):
    time__time_slots   = serializers.IntegerField()
    table       = serializers.IntegerField()
    class Meta:
        model   = TimeSlotsModel
        fields  = ('time__time_slots', 'table')

class TablesSerializer(serializers.Serializer):
    table = serializers.IntegerField()
    class Meta:
        model   = TablesModel
        fields  = ('table',)
