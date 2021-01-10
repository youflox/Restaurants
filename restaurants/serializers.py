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
        fields = ('__all__')
        read_only_fields = ('id',)

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
    # AJAX  data    {'table': 10, 'date': '10-10-2021', 'slots': 4, 'restaurant': 3}
    
    slots   = serializers.IntegerField()
    date    = serializers.CharField()
    restaurant = serializers.IntegerField()

    class Meta:
        model = TablesModel
        fields = ('date', 'slots', 'restaurant', 'table')


    def save(self, instance, validated_data):
# 1 {'date': '10-10-2021', 'slots': 2, 'restaurant': 3, 'table': 10}

        print(validated_data,"restaurant")

        date        = DateModel(date=validated_data['date'],
                            user_id=instance,
                            restaurant_id=validated_data['restaurant']
                        )

        print(date)

        timeslot    = TimeSlotsModel(date=date, slots=validated_data['slots'])

        print(timeslot)
        
        table       = TablesModel(time=timeslot, table=validated_data['table']) 

        print(table)

        date.save()
        timeslot.save()
        table.save()

        print(date)