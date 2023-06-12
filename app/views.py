from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CountrySerializer
from .models import *
# Create your views here.

#creatting api for fetching of data form database
class CountryView(APIView):
    def get(self,request):
        country = Country.objects.all()
        serializer = CountrySerializer(country,many=True)
        data  = serializer.data
        return Response(data,status=200)
    
def index(request):
    return render(request,'index.html')


