from django.shortcuts import render
from django.shortcuts import get_object_or_404

from restaurants.models import RestaurantModel


# Create your views here.

def restaurent_view(request):
    return render(request, 'restaurent_view.html')


def booking_view(request,id):
    queryset = RestaurantModel.objects.all()
    resta    = get_object_or_404(queryset, id=id)
   
    ctx = {'data' : resta}

    print(ctx['data'].id)

    return render(request, 'booking_view.html', ctx)