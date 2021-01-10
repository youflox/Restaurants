from rest_framework import serializers

from .models import (
    RestaurantModel,
    RatingModel,
    TimeSlotsModel,
    TablesModel,
    DateModel,
)

class DateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DateModel
        exclude = ('user',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model   = RatingModel
        fields  = '__all__'

class RestaurentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantModel
        fields = ('id','name','image','category','price','ratings')
        read_only_fields = ['ratings',]

class TablesSerializer(serializers.Serializer):
    table = serializers.IntegerField()
    class Meta:
        model   = TablesModel
        fields  = ('table',)

class TimeSlotsSeializer(serializers.ModelSerializer):
    
    table = serializers.IntegerField()
    class Meta:
        model   = TimeSlotsModel
        fields  = ('slots', 'table')


class NewBookingSerializer(serializers.ModelSerializer):
    # AJAX  data    {'table': 10, 'date': '10-10-2021', 'timeslot': 4, 'restaurant': 3}
    
    date         = DateModelSerializer()
    timeslot     = TimeSlotsSeializer()

    class Meta:
        model   = TablesModel
        fields  = ('date', 'timeslot', 'table')

        def save(self, instance, validated_data):
            pass