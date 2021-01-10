from django.shortcuts import render, get_object_or_404
from django.db.models import F, Q

from rest_framework.response import Response
from rest_framework.views import APIView 

from .models import (
    RestaurantModel, 
    RatingModel, 
    TimeSlotsModel,
    DateModel,
    TablesModel,
)

from .serializers import (
    RestaurentModelSerializer, 
    RatingSerializer,
    TimeSlotsSeializer,
    TablesSerializer,
    NewBookingSerializer,
)

import json

# Create your view here.

class RestaurentRegisterView(APIView):
    """
    To register a new restaurent APIVIew
    """
    serializer_class  = RestaurentModelSerializer

    def post(self, request):
        data    = request.data
        serializer  = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        return Response(user_data)

#Lisint all the Restaurants
class RestaurantView(APIView):
    """
    For listing all the Restaurents.
    """
    serializer_class  = RestaurentModelSerializer

    def get(self, request, pk=None):
        if pk:
            queryset    = RestaurantModel.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer  = self.serializer_class(user)
        else:
            queryset    = RestaurantModel.objects.all()
            serializer  = self.serializer_class(queryset, many=True)
            
        return Response(serializer.data)

#Not using 
class Ratings(APIView):
    serializer_class = RatingSerializer

    def get(self,request):
        data = RatingModel.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)



#  Using This To Render Slots and Table data in Vue
class TimeSlotsView(APIView):
    serializer_class = TimeSlotsSeializer

    def get(self, request, date, restaurent):
        date = DateModel.objects.filter(
            Q(date=date) &
            Q(restaurant = restaurent)
        ).values_list('id', flat=True)
       
        if date:
            query = TablesModel.objects.select_related('time', 'time__date').values('time', 'time__date').filter(time__date__in=date).values('table', slots=F('time__slots'))    
            # query = TablesModel.objects.all().prefetch_related('time').filter(time__date=date.id).values('table', slots=F('time__slots'))          
            serializer  = self.serializer_class(query, many=True)
            data = serializer.data        
        else:
            data = {'Response' : 'No records found'}
        return Response(data)

class TablesView(APIView):
    """
    Check filled tables
    """
    serializer_class = TablesSerializer

    def get(self, request,date, restaurent, time):
        data = TablesModel.objects.select_related('time').values('table').filter(time__slots = time)

        print(data)

        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)    
    

#Create a new Booking
class NewBooking(APIView):
    """
    New Booking Post request
    """
    serializer_class = NewBookingSerializer

    def post(self, request):        
        req =request.data
        serializer = self.serializer_class(req)
        return Response(serializer.data)
        # return Response({'msg':req})
