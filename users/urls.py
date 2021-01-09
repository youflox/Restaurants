from django.contrib import admin
from django.urls import path, include

from .views import RegisterView

urlpatterns = [
   path('', RegisterView.as_view())
]
