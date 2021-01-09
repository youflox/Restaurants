from django.contrib import admin
from django.urls import path, include

from .views import restaurent_view, booking_view

urlpatterns = [
   path('', restaurent_view, name='restuarents'),
   
   path('booking/<int:id>/', booking_view, name='booking')

]
