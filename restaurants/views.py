from django.shortcuts import render, get_object_or_404
from django.db.models import Q

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
)

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


class Ratings(APIView):
    serializer_class = RatingSerializer

    def get(self,request):
        data = RatingModel.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class TimeSlotsView(APIView):
    serializer_class = TimeSlotsSeializer

    def get(self, request, date, restaurent):

        date = DateModel.objects.filter(
            Q(date=date) &
            Q(restaurant_date = restaurent)
        ).first()      

        if date:
            query = TablesModel.objects.all().prefetch_related('time', 'time__date', 'time__date__restaurant_date').filter(time__date=date.id).values('time__time_slots','table')
            serializer  = self.serializer_class(query, many=True)
            data = serializer.data
        else:
            data = {'Response' : 'No records found'}
        return Response(data)

class TablesView(APIView):
    """
    Check filled
    """

    serializer_class = TablesSerializer

    def get(self, request,date, restaurent, time):
        data = TablesModel.objects.select_related('time').values('table').filter(time__time_slots = time)
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)    
    