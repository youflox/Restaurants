from django.contrib import admin
from django.urls import path, include

from .views import (
    RestaurantView, 
    RestaurentRegisterView, 
    Ratings, 
    TimeSlotsView,
    TablesView,
    NewBooking
)

urlpatterns = [
    path('', RestaurantView.as_view()),
    path('<int:pk>/', RestaurantView.as_view()),

    path('register/', RestaurentRegisterView.as_view()),
    path('ratings/', Ratings.as_view()),
    path('timeslot/<str:date>/<int:restaurent>/', TimeSlotsView.as_view()),
    path('timeslot/<str:date>/<int:restaurent>/<int:time>/', TablesView.as_view()), 
    
    path('booking/', NewBooking.as_view()), 

]

        # print(request.user.id, restaurent, date, slot, table)
