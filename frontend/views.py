from django.shortcuts import render
from django.shortcuts import get_object_or_404

from restaurants.models import RestaurantModel


# Create your views here.

def restaurent_view(request):
    return render(request, 'restaurent_view.html')


def booking_view(request,id):
    resta = RestaurantModel.objects.filter(id=id).first()
    user  = request.user.username

    ctx = {'data' : resta, 'user' : user}
    
    return render(request, 'booking_view.html', ctx)