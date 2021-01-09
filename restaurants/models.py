from django.db import models
from django.contrib.auth.models import User

# Create your models here.

categories = (
    ("OUTDOOR", "OUTDOOR"),
    ("CAFE", "CAFE"),
    ("PUB & BAR", "PUB & BAR"),
    ("BUFFET", "BUFFET"),
    ("FAMILY DINING", "FAMILY DINING"),
)

class RestaurantModel(models.Model):
    # Name, image, category, price
    name        = models.CharField(max_length=100, unique=True)
    image       = models.ImageField(upload_to='images', blank=True, height_field=None, width_field=None, max_length=100)
    price       = models.IntegerField(default=400)
    tables      = models.IntegerField(default=5)
    ratings      = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    category    = models.CharField(max_length=100, choices=categories, default="0")

    def __str__(self):
        return self.name


class RatingModel(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE,related_name='ratingmodeluser', blank=True, null=True)
    rating              = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    restaurant_rating   = models.OneToOneField(RestaurantModel, related_name='restaurant_rating', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.rating)


class DateModel(models.Model):
    date            = models.CharField(max_length=50)
    user            = models.ForeignKey(User, on_delete=models.CASCADE,related_name='date_user', blank=True, null=True)
    restaurant_date = models.ForeignKey(RestaurantModel, related_name='restaurant_date', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.date


class TimeSlotsModel(models.Model):
    date        = models.ForeignKey(DateModel, related_name='slotpicker', on_delete=models.CASCADE, blank=True, null=True)
    time_slots  = models.CharField(max_length=50)

    def __str__(self):
        return self.time_slots


class TablesModel(models.Model):
    table   = models.IntegerField()
    time    = models.ForeignKey(TimeSlotsModel,on_delete=models.CASCADE,related_name='table_time', blank=True, null=True)

    def __str__(self):
        return str(self.table)