from django.contrib import admin

from .models import (
    TimeSlotsModel, 
    DateModel, 
    RestaurantModel, 
    RatingModel,
    TablesModel,
)


# Register your models here.

@admin.register(TablesModel)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'table', 'time']


@admin.register(TimeSlotsModel)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_slots', 'date']
    

@admin.register(DateModel)
class DateAdmin(admin.ModelAdmin):
    list_display =['id', 'date', 'user', 'restaurant_date']


@admin.register(RatingModel)
class RatingAdmin(admin.ModelAdmin):
    list_display =['id', 'rating', 'user', 'restaurant_rating']


@admin.register(RestaurantModel)
class RestaurantAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'tables', 'ratings']
